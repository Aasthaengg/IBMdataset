K, T = map(int, input().split())

As = list(map(int, input().split()))

a = max(As)

print(max(2*a-K-1,0))