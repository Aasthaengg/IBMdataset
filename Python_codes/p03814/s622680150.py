import sys
l = list(sys.stdin.readline().rstrip("\n"))
a = 10000000
z = 0
for i,s in enumerate(l):
    if s == 'A':
        a = min(a,i)
    if s == 'Z':
        z = i
print(z-a+1)