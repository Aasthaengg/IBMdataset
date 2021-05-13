N, K = input().split()
IK = int(K)
P = list(map(int, input().split()))
Sorted_P = sorted(P)
S = 0
i = 0

while i < IK:
    S = S + Sorted_P[i]
    i = i + 1


print(S)