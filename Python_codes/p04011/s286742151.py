s = [int(input()) for i in range(4)]
if s[0] <= s[1]:
    ans = s[0]*s[2]
else:
    ans = s[1]*s[2]+(s[0] - s[1])*s[3]
print(ans)
