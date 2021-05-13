H, N = map(int, input().split())
a = list(map(int, input().split()))

if H > sum(a):
    print("No")
else:
    print("Yes")
