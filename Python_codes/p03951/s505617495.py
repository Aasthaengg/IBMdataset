N = int(input())
s = input()
t = input()
ans = 2*N
for i in range(N):
    if s[i:N] != t[0:N-i]:
        continue
    ans = N+i
    break
print(ans)
