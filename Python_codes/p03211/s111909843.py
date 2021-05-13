s = str(input())
arr = [int(s[i:i + 3]) for i in range(len(s) - 2)]
ans = []
for i in arr:
    ans.append(abs(753 - i))
print(min(ans))