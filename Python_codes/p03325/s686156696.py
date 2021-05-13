n = int(input())
A = tuple(map(int, input().split()))

fac2num = []
for a in A:
    c = 0 
    while a%2 == 0:
        a //= 2
        c += 1
    fac2num.append(c)
print(sum(fac2num))
