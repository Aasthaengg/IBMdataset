n = int(input())
s = input()
x = 0
ans = 0
for si in s:
    x += (si == "I")
    x -= (si == "D")
    ans = max(ans,x)
print(ans)