n,w = map(int,input().split())
wv = [[int(i) for i in input().split()] for j in range(n)]

wv.sort(key=lambda x:(x[0],-x[1]))
#print(wv)
#exit()
#wv.sort()
min_v = wv[0][0]
cnt = 0
num = [0]*4

for i in range(n):
    num[wv[i][0] - min_v] +=1
        
#dp = [[[0 for i in range(n)] for j in range(n)] for k in range(n)]

#print(wv)

t_num3 = [0]
tmp = 0
for i in range(num[3]):
    tmp += wv[n-num[3]+i][1]
    t_num3.append(tmp)

#print(t_num3)
#exit()

t_ans = 0
t_num0 = 0
ans = 0


for i in range(num[0]+1):
    if i != 0:
        t_num0 += wv[i-1][1]
    #print(t_ans,i)
    t_num1 = 0
    for j in range(num[1]+1):
        if j != 0:
            t_num1 += wv[num[0]+j-1][1]
        t_num2 = 0
        for k in range(num[2]+1):
            if k != 0:
                t_num2 += wv[num[0]+num[1]+k-1][1]
            ima_w = min_v*(i+j+k) + 1*j+2*k
            idx = (w - ima_w)//(min_v+3)
            if ima_w > w:
                break
            else:
                t_ans = t_num0+t_num1+t_num2 + t_num3[min(idx,num[3])]
        #print(t_ans)
            ans = max(t_ans,ans)

print(ans)