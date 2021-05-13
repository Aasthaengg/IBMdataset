s = input()
l = len(s)
half = l//2
check = 0
for i in range(half):
    if s[i] != s[l-1-i]:
        check += 1
print(check)