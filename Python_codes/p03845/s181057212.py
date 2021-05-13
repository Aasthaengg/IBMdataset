N = int(input())
Nl = list(map(int, input().split()))
s = sum(Nl)

M = int(input())
for i in range(M):
    Ml = list(map(int, input().split()))
    print(s + Ml[1] - Nl[Ml[0] - 1])