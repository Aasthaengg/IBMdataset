N = int(input())
P = [int(x) for x in input().split()]

Count = 0
for T in range(0,N-2):
    if P[T+1] == sorted(P[T:T+3])[1]:
        Count += 1
print(Count)