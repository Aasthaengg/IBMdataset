N = int(input())
s = input()
t = input()
for i in range(N):
    ok = 1
    for j in range(N-i):
        if s[i+j] != t[j]:
            ok = 0
            break
    if ok == 1:
        ans = N+i
        break
if ok == 0:
    ans = 2*N
print(ans)
