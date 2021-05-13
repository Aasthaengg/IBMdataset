n = int(input())
A = list(map(int , input().split()))
q = int(input())
B = list(map(int , input().split()))

ans = []

for bit in range(1<<n):
    tmp = 0
    for i in range(n):
        if bit & (1<<i):
            tmp += A[i]
    ans.append(tmp)

for j in range(q):
    if B[j] in ans:
        print("yes")
    else:
        print("no")
