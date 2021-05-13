n = int(input())
a = [ int(x) for x in input().split() ]
b = [ int(x) for x in input().split() ]
c = [ int(x) for x in input().split() ]

k = 0
i = -1

for e in a:
    k += b[e - 1]
    if i == e-1:
        k += c[i - 1]

    i = e

print(k)
