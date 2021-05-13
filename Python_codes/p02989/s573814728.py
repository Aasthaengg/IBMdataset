a = int(input()) // 2
N = input().split(" ")
N = (int(s) for s in N)
N = sorted(N)
bet = N[a] - N[a - 1]
print(bet)
