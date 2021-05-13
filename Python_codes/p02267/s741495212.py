n = int(input())
S = [int(i) for i in input().split()]
q = int(input())
T = [int(i) for i in input().split()]
C = 0
for i in T:
    for j in S:
        if j == i:
            C += 1
            break
print(C)