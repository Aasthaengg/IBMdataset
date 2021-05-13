n = int(input())
s, t = input().split()

ans = ""
for ss, tt in zip(s, t):
    ans += ss + tt
print(ans)