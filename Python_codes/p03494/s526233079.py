n = int(input())
a = list(map(int, input().split()))
ans = 0
for ans in range(31):
    for i,A in enumerate(a):
        if A%2:
            print(ans)
            exit()
        a[i] //= 2
