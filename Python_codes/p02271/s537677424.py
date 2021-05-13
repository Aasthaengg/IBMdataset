n = int(input())
A = list(map(int, input().split()))
q = int(input())
M = list(map(int, input().split()))

ans = set()
for i in range(2**n):
    total = 0
    bits = bin(i)[2:].zfill(n)
    for j, b in enumerate(bits):
        if b == '1':
            total += A[j]
    ans.add(total)

for i in range(q):
    if M[i] in ans:
        print('yes')
    else:
        print('no')

