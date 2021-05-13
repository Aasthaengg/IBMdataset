# B - Collatz Problem
s = int(input())
a = s
S = set([s])
for i in range(2,10**6+1):
    a = a//2 if a%2==0 else 3*a+1
    if a in S:
        print(i)
        break
    S.add(a)