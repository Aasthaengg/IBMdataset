s = input()
n = len(s)
ans = float("inf")
for i in range(n-2):
    ans = min(ans,abs(eval(s[i:i+3])-753))
print(ans)