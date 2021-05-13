N = int(input())
A = [0] + list(map(int, input().split())) + [0]

len = []
for i in range(N+1):
    len.append(abs(A[i+1]-A[i]))

sum = sum(len)
ans = sum

for i in range(N):
    ans -= (len[i]+len[i+1])
    ans += abs(A[i+2]-A[i])
    print(ans)
    ans = sum
