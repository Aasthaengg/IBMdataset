N, K = map(int, input().split())

has_snack = [False]*N

for _ in range(K):
    d = int(input())
    A = list(map(int, input().split()))
    for a in A:
        has_snack[a-1] = True

print(sum([1 for h in has_snack if h == False]))
