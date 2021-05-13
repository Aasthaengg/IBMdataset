import sys
sys.stdin.readline

N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
sa = []
sa_a = 0
sa_b = []
sa_c = 0
count = 0

for i in range(N):
    sa.append(A[i]-B[i])

sa.sort()

if sum(sa) <= 0:
    print(-1)
    sys.exit()
else:
    for i in range(N):
        if sa[i] < 0:
            count += 1
            sa_a += abs(sa[i])
        else:
            sa_b.append(sa[i])

while sa_a > sa_c:
    sa_c += sa_b.pop()
    count += 1

print(count)
