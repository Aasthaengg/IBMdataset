s = list(input())
l = len(s)
a = ''
if l%2 != 0:
    for i in range(l//2+1):
        a = a + "".join(s[2*i])
else:
    for i in range(l//2):
        a = a + "".join(s[2*i])
print(a)