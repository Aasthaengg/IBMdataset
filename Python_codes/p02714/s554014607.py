n = int(input())
c = list(input())

r = c.count("R")
g = c.count("G")
b = c.count("B")

ans = r*g*b
count  = 0
sub1 = 0

for i in range(n):
    for j in range(i+1,n):
        if 2*j-i >= n or 2*j-i <0:
            break
        elif c[2*j-i] != c[i] and c[i] != c[j] and c[2*j-i] != c[j]:
                sub1 += 1


print(ans-sub1)
