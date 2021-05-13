n = int(input())
al = list(map(int,input().split()))

pos = ""
max_abs = 0
value = ""
for idx, a in enumerate(al):
    if abs(a) >= max_abs:
        pos = idx + 1 
        max_abs = abs(a)
        value = a

print(2*n - 2)
if value >= 0:
    print(pos)
    print(2)
    print(pos)
    print(2)
    for i in range(2, n):
        print(i)
        print(i+1)
        print(i)
        print(i+1)

else:
    print(pos)
    print(n-1)
    print(pos)
    print(n-1)
    for i in range(n-1, 1, -1):
        print(i)
        print(i-1)
        print(i)
        print(i-1)