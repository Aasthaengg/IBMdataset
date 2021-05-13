
s = input()

if len(s) != 1:
    ans = [0] *(round(len(s)/2))
else:
    ans = [0]

ind = 0
for i in range(len(s)):

    if (i+1) % 2 == 1:
        ans[ind] =str( s[i])
        ind += 1

ans = ''.join(ans)
print(str(ans))
