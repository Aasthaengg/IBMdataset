N = int(input())
D = list(map(int, input().split()))

d_sorted = sorted(D)

na = d_sorted[int(N/2)]
nb = d_sorted[int(N/2-1)]

print(na-nb)

