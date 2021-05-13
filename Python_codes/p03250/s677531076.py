N = list(map(int, input().split()))

N = sorted(N, reverse=True)
print(N[0]*10 + N[1] + N[2])
