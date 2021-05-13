N = int(input())

R = []

for i in range(N):
    S,P = input().split()
    R.append([S, -int(P), i+1])

R.sort()

for r in R:
    print(r[2])