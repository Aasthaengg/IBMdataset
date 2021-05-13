s = input()
k = int(input())
alp = 'bcdefghijklmnopqrstuvwxyza'
t = alp.find(s[0])
if len(s) == 1:
    s = alp[(k+t)%26]
else: 
    if k >= 25-t:
        s = 'a' + s[1:]
        k -= 25-t
    for i in range(1, len(s)-1):
        t = alp.find(s[i])
        if k >= 25-t:
            s = s[:i] + 'a' + s[i+1:]
            k -= 25-t
    s = s[:len(s)-1] + alp[(k+alp.find(s[-1]))%26]
print(s)