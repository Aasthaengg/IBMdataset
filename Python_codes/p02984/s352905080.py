from itertools import accumulate
N = int(input())
A = list(map(int, input().split()))
S = list(accumulate([0] + [(1-2*(i%2))*a for i, a in enumerate(A)]))
print(*[(1-2*(i%2))*((S[N]-S[i]) - (S[i]-S[0])) for i in range(N)])
