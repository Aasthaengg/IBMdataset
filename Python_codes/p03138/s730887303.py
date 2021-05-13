n,k = map(int,input().split())
ai = [int(i) for i in input().split()]

tmp = format(max(k,max(ai)), 'b')

lng = len(tmp)
tmp = format(k, '0'+str(lng)+'b')

li = [0]*(lng)
ai_li = [0]*(n)

for i in range(n):
    #print(i)
    #print(ai[i])
    #print(format(ai[i], '0'+str(lng)+'b'))
    ai_li[i] = format(ai[i], '0'+str(lng)+'b')

add_enb_flag = False

for i in range(lng):
    cnt = 0
    for j in range(n):
        if ai_li[j][i] == '1':
            cnt += 1
    #print(cnt,i)
    if cnt >= (n+1) // 2:
        if tmp[i] == "1":
            add_enb_flag = True
        li[i] = 0
    elif tmp[i] == '1' or add_enb_flag == True:
        li[i] = 1
    else:
        li[i] = 0
k_m = 0
bai = 1

for i in range(lng):
    k_m += li[lng-i-1] *bai
    bai *= 2

#print(k_m,ai_li,tmp,li)
        
ans = 0
for i in range(n):
    ans += k_m^ai[i]
    
print(ans)