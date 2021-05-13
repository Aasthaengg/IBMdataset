n = int(input())

l = []
a = []
for i in range(n):
    s = int(input())
    l.append(s)
    if s%10 != 0:
        a.append(s)

S = sum(l)
    
if S%10 != 0:
    print(S)
elif len(a) >= 1:
    print(S-min(a))
else:
    print(0)