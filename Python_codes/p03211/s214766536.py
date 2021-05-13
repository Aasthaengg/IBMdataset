s = input()
l, ans = len(s), []
for i in range(0,l-2):
    n = s[i:i+3]
    ans.append(abs(753-int(n)))
print(min(ans))