N = int(input())
s = input()
t = input()

max_i = 0
for i in range(N+1):
    if s[N-i:] == t[:i]:
        max_i = i

ans = s[:N-max_i] + t
print(len(ans))
