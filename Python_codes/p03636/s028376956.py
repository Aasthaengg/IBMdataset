s = list(input())
ans = s[0]
ans += str(len(s[1:-1]))
ans += s[-1]
print(ans)