N = int(input())
A = list(map(int,input().split()))

dic = {}
for i in range(N):
    data = i + 1 + A[i]
    if data in dic:
        dic[data] += 1
    else:
        dic[data] = 1
        
ans = 0
for i in range(N):
    res = i + 1 - A[i]
    if res in dic:  ans += dic[res]
print(ans)