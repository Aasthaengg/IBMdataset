Q, H, S, D = map(int, input().split())
N = int(input())
single = min(Q * 4, H * 2, S)
div, mod = divmod(N, 2)
print(min(single * N, int(D * div) + int(single * mod)))
