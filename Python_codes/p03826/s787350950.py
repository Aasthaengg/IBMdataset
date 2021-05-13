from sys import stdin
def LI(): return list(map(int,stdin.readline().rstrip().split()))

tmp = LI()

a,b,c,d = [tmp.pop(0) for i in range(4)]

s1 = a*b
s2 = c*d

if s1 < s2:
    print(s2)
else:
    print(s1)