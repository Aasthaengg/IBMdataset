N = int(input())
A = list(map(int,input().split()))
c = 0
for e in A:
    if e%2 == 1:
        c += 1
if c%2 == 1:
    print("NO")
else:
    print("YES")
