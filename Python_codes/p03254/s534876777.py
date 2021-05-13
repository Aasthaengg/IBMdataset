n, x = map(int, input().split())
A = sorted(list(map(int, input().split())))
for i in range(n + 1):
    if sum(A[:i]) > x:
        print(i - 1)
        exit()
    elif sum(A[:i]) == x:
        print(i)
        exit()
print(n - 1)