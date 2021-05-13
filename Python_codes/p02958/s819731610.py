n = int(input())
s = list(map(int, input().split()))
t = sorted(s)
cnt = 0
for i in range(n):
    if s[i] != t[i]:
        cnt += 1
print("YES" if cnt <= 2 else "NO")
