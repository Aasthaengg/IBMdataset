s = list(map(str,input().split()))
ans = []
for i in range(3):
    ans.append(s[i][0].upper())
print("".join(ans))
