n,c = map(int,input().split())
stc = [[int(i) for i in input().split()] for j in range(n)]

ans = 0

stc.sort(key=lambda x:(x[2],x[1],x[0]))

time = 10**5+1

c_imos = [[0 for i in range(time)] for j in range(c)]

for i in range(n):
    for j in range(stc[i][1]-stc[i][0]+1):
        c_imos[stc[i][2]-1][stc[i][0]-1+j] = 1


"""
for i in range(n):
    c_imos[stc[i][2]-1][stc[i][0]-1] += 1
    c_imos[stc[i][2]-1][stc[i][1]] -= 1
"""
#nd_v = [[0 for i in range(time)] for j in range(c)]
"""
for i in range(c):
    for j in range(time):
        if j == 0:
            if c_imos[i][j] == 1:
                nd_v[i][j] = 1
        else:
            nd_v[i][j] = nd_v[i][j-1] + c_imos[i][j]
"""
"""
for i in range(c):
    for j in range(time):
        if nd_v[i][j] >= 2:
            nd_v[i][j] = 1
"""
ans = 1

#print(c_imos)

for i in range(time):
    tmp = 0
    for j in range(c):
        tmp += c_imos[j][i]
    #print(i,tmp)
    ans = max(tmp,ans)

print(ans)

exit()
    
c_num = stc[0][2]
t_num = stc[0][1]
idx = 0
print(stc)
for i in range(1,n):
    print(t_num,i)
    if stc[idx+i][2] == c_num:
        if stc[idx+i][0] == t_num:
            stc[idx+i-1][1] = stc[idx+i][1]
            t_num = stc[idx+i][1]
            del stc[idx+i]
            idx -= 1
        else:
            print(t_num,t_num,t_num)
            c_num = stc[idx+i][2]
            t_num = stc[idx+i][1]

stc.sort(key=lambda x:x[1])
print(stc)
exit()
tmp = stc[0][1]

ans = 1
ans_tmp = 1

for i in range(1,len(stc)):
    for j in range(i+1,len(stc)):
        if tmp >= stc[j][0]:
            ans_tmp += 1
        else:
            tmp = stc[j][0]
            ans = max(ans_tmp,ans)