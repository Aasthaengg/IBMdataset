N = int(input())
A = [int(input()) for _ in range(N)]
dic = {}
for i in range(N):
    data = A[i]
    if data in dic:  dic[data] += 1
    else:  dic[data] = 1
ans = 0
for i in dic:
    if dic[i] % 2:  ans += 1
print(ans)