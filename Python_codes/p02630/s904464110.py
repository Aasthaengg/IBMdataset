li = [0]*(10**5+1)

N = int(input())
A = [int(i) for i in input().split()]
p = sum(A)

for i in A:
    li[i] += 1

ans = []
Q = int(input())
for i in range(Q):
    B,C = [int(zz) for zz in input().split()]
    p += (C-B)*li[B]
    li[C] += li[B]
    li[B] = 0
    ans.append(p)

[print(i) for i in ans]
