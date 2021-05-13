n,k = map(int,input().split())
li = list(map(int,input().split()))
ans = [0]*(n+1)
tmp = [0]*(n+1)
tmp_sum = []
#print(ans)
#[0, 0, 0, 0, 0]
k = min(k,100)

for kkk in range(k):
    #print(li,'li')
    for i,l in enumerate(li):
        if l != 0:
            start = max(0,i-l)
            end = min(n,i+l+1)
            #print(start,'start',end,'end')
            tmp[start] += 1
            #print(end,len(tmp),'aaa')
            tmp[end] -= 1
    #print(tmp,'tmp')
    last = 0
    for t in tmp:
        last = t+last
        tmp_sum.append(last)
    for i,l in enumerate(li):
        if l == 0:
            tmp_sum[i] += 1
    ans = tmp_sum[:n]
    li = tmp_sum[:n]
    tmp = [0]*(n+1)
    tmp_sum = []
    #if len(set(ans)) == 1:
    #    break
print(*ans)