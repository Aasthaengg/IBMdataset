s = input()

ans = 1000000
for i in range(len(s)-1):
    ans = min(ans, abs(int(s[i:i+3]) - 753))
print(ans)