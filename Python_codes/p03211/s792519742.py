s = input()
min = 100000000000
for i in range(2, len(s)):
    x = 100*int(s[i-2])+10*int(s[i-1])+int(s[i])
    ans = abs(x-753)
    if min > ans: min = ans
print(min)