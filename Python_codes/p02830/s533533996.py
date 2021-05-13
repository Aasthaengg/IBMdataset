N = int(input())
S, T = input().split()
ans = ''
for s, t in zip(list(S), list(T)):
    ans += s + t
print(ans)