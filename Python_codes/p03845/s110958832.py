N = int(input())
T = list(map(int, input().split()))
total = sum(T)
for _ in range(int(input())):
    P, X = map(int, input().split())
    print(total - T[P - 1] + X)
