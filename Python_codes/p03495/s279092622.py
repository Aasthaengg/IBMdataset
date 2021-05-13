N, K = list(map(int,input().split()))
A = list(map(int,input().split()))
dic = {}
for i in range(N):
    data = A[i]
    if data in dic:  dic[data] += 1
    else:  dic[data] = 1
dic = sorted(dic.values())
ans = 0
l = len(dic)
for i in range(l - K):
    ans += dic[i]
print(ans)