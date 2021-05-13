N = int(input())
F = []
for _ in range(N):
    F.append(input().split())
P = []
for _ in range(N):
    P.append(list(map(int,input().split())))

def return_C(i, List):
    j = ''.join(List)
    j = int(j, 2)
    AND = i & j
    return bin(AND).count('1')

ans = - 10 ** 10
for i in range(1, 2 ** 10):
    temp = 0
    for j in range(N):
        c = return_C(i, F[j])
        temp += P[j][c]
    ans = max(ans, temp)

print(ans)