n = int(input())
A, B = zip(*[tuple(map(int, input().split()))for _ in range(n)])
cnt = 0
for a, b in zip(A[::-1], B[::-1]):
    cnt += -(-(cnt+a)//b)*b-(cnt+a)
print(cnt)
