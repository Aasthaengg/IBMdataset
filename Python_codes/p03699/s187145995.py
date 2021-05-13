n = int(input())
s = [0]*n
for i in range(n):
    s[i] = int(input())
t = sum(s)
s = sorted(s)
a = [-1]*n
for i in range(n):
    if s[i] % 10 != 0:
        a[i] = i
if t%10 == 0:
    sw = 1
    for i in range(n):
        if a[i] != -1:
            t -= s[a[i]]
            sw = 0
            break
    if sw == 1:
        t = 0
print(t)