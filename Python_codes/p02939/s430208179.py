s = input()
ans = 0
c = ''
b = ''
for i in list(s):
    c += i
    if c != b:
        ans += 1
        b = c
        c = ''
print(ans) 