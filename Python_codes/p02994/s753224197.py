n,l=map(int,input().split())

s1 = 0
m1 = 10**8

for i in range(n):
    if abs(m1) > abs(l):
        m1 = l
    s1 += l
    l += 1

print(s1 - m1)