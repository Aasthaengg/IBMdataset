n = int(input())
A = list(map(int, input().split()))
q = int(input())
M = list(map(int, input().split()))
mans = set()
b = 0
for b in range(2**n):
    ans = 0
    for i in range(n):
        if 1&(b>>i):
            ans += A[i]
    mans.add(ans)
for m in M:
    if m in mans:
        print("yes")
    else:
        print("no")
