n = int(input())
a = 0
b = 0
c = 0
total = 0
for _ in range(n):
    s = input()
    total += s.count('AB')
    if s[0] == 'B' and s[-1] == 'A':
        c+=1
    elif s[-1] == 'A':
        a+=1
    elif s[0] == 'B':
        b+=1

if a+b == 0:
    print(total + max(0, c - 1))
else:
    print(total + min(a, b) + c)


