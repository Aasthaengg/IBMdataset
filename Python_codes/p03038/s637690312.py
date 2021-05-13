N,M = map(int,input().split())

A = list(map(int,input().split()))
A.sort(reverse=True)
BC = []
for _ in range(M):
    B, C = (int(x) for x in input().split())
    BC.append([B, C])
BC = sorted(BC, key=lambda x: -x[1])

index = 0

ans = 0

while index < M and len(A) and A[-1] < BC[index][1]:
    b, c = BC[index]
    count = 0
    while len(A) and A[-1] < c and count < b:
        A.pop()
        ans += c
        count += 1
    index += 1
print(sum(A)+ans)