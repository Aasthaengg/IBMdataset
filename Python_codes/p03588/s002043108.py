n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.sort(reverse = True)
print(a[0][0] + a[0][1])