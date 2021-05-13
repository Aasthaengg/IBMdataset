n = int(input())
s = input()
t = input()

c = 0
for i in range(n):
    d = t[:i]
    if d in s:
        c = i
if s == t:
    print(n)
else:
    print(2*n-c)