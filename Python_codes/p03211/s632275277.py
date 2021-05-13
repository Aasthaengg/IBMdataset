s = input()
s_size = len(s)
ans = float('inf')
for i in range(s_size-2):
    ans = min(abs(753-int(s[i]+s[i+1]+s[i+2])), ans)
print(ans)