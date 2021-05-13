n=int(input())
s = input()
l = list(s)
L = []

for i in l:
    m = ord(i)
    if m + n <= 90:
        i = chr(m + n)
        L += i
    if m + n > 90:
        i = chr(m+n -26)
        L += i

print(''.join(L))