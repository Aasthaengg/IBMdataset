n, p = map(int, input().split())
A = list(map(int, input().split()))
if all(a % 2 == 0 for a in A):
    if p:
        print(0)
    else:
        print(pow(2, n))
else:
    print(pow(2, n-1))
