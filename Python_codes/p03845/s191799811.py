n = int(input())
T = list(map(int, input().split()))
m = int(input())
s = sum(T)
for _ in range(m):
    p, x = map(int, input().split())
    print(s - T[p-1] + x)