n = int(input())
A = list(map(int, input().split()))
A = sorted(A)

if n % 2 == 0:
    total = 0
    for i in A[::-1][:n//2]:
        total += i*2
    total = total - A[-1]
    print(total)
else:
    total = 0
    for i in A[::-1][:n//2+1]:
        total += i*2
    total = total - A[-1]
    total = total - A[-(n//2+1)]
    print(total)