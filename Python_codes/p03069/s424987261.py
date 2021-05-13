n = int(input())
s = input()
wcount = 0
min_val = 0
for i in range(n):
    if s[i] == '.':
        wcount += 1
    min_val = min(min_val, i + 1 - wcount * 2)
print(wcount + min_val)
