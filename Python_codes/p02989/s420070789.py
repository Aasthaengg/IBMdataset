n = int(input())
d = list(map(int, input().split()))
d.sort()

half = int(n/2)

n1 = d[half-1]
n2 = d[half]

if n2-n1 == 0:
    print(0)
    exit()
else: 
    print(n2-n1)