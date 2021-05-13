s = list(input())
ans = ""
w = int(input())
for i in range(0,len(s),w):
    ans += s[i]
print(ans)