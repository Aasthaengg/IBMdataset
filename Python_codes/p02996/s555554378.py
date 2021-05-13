n = int(input())
ab = [list(map(int, input().split())) for i in range(n)]
a = 0

sortsecond = lambda x: x[1]
ab.sort(key = sortsecond)

for i in range(n):
    a += ab[i][0]
    if a > ab[i][1]:
        print("No")
        exit()
print("Yes")