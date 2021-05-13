n, c, k = map(int, input().split())

lt = list()
for i in range(n):
    lt.append(int(input()))
lt.sort()

b = 1  #the number of buses
p = 0  #passengers
m = lt[0]

for i in range(n):
    if p < c and lt[i]-m <= k:
        p += 1
    else:
        p = 1
        b += 1
        m = lt[i]

print(b)