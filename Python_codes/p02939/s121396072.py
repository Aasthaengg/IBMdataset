s = input()
num = len(s)
i, ans = 0, 0
while i < num-1:
    if s[i] != s[i+1]:
        ans += 1
        i += 1
    else:
        if i == num-2: ans += 1
        else: ans += 2
        i += 3
if num == 1: print(1)
elif i == num-1: print(ans+1)
else: print(ans)
    

