from sys import stdin

n, a, b = [int(x) for x in stdin.readline().rstrip().split()]

s = 0
for i in range(n+1):
    pp = 0
    m = i
    for j in range(5):
        p = m % 10
        pp = pp + p
        m = m//10
    if pp >= a and pp <= b: s = s + i

print (s)



