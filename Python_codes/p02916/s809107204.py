N = int(input())
LA = list(map(int, input().split()))
LB = list(map(int, input().split()))
LC = list(map(int, input().split()))

SFB = sum(LB)
SFC = 0

for i in range(1, N):
    j = i - 1
    if LA[i] == (LA[j] + 1):
        A = LA[i] - 2
        SFC += LC[A]

print(SFB + SFC)