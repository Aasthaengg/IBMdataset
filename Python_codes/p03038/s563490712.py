n, m = map(int, input().split())
A = list(map(int, input().split()))
BC = [list(map(int, input().split())) for _ in range(m)]

A.sort()
BC.sort(key=lambda x:x[1], reverse=True)

pos = 0
for b, c in BC:
    end = (pos + b) if pos + b <= n else n
    for i in range(pos, end):
        if A[i] < c:
            A[i] = c
        else:
            break
    pos = i + 1
    if pos >= n:
        break

print(sum(A))