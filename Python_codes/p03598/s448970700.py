N = int(input())
K  = int(input())
li = list(map(int,input().split()))	
ans = []
for i in range(N):
    if abs(li[i]-0)>=abs(li[i]-K):
        ans.append(2*abs(li[i]-K))
    elif abs(li[i]-0)<abs(li[i]-K):
        ans.append(2*li[i])
print(sum(ans))