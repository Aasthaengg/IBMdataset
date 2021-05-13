N = int(input())
A = [int(i) for i in input().split()]; A.sort()

B = []; b = 0
for i in A:
    b += i
    B.append(b)

c = 1; w = True
while w:
    if 2*B[N-1-c] >= A[N-c]:
        c += 1
        if c == N: break
    else:
        w = False

print(c)
