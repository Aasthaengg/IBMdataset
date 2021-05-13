import sys
n, m, k = map(int, input().split())

if k==0:
    print("Yes")
    sys.exit()

for i in range(n+1):
    black=i*m
    c=n-(2*i)
    for j in range(m+1):
        if black+(j*c)==k:
            print("Yes")
            sys.exit()

print("No")