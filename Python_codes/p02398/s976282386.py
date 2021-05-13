m = map(int,raw_input().split())
a = m[0]
b = m[1]
c = m[2]
n = 0

for i in range(a,b+1):
    if c % i == 0:
        n += 1
print n