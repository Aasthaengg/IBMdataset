g=0
e=0
n=int(input())
for i in range(n):
    p=int(input())
    e=e+p
    if g<p:
        g=p
print((g//2)+(e-g))