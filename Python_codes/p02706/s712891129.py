#k = int(input())
#s = input()
#a, b = map(int, input().split())
#l = list(map(int, input().split()))

n, m = map(int, input().split())
a = list(map(int, input().split()))


for i in range(m):
    n = n - a[i]
    if (n < 0):
        print(-1)
        exit()

print(n)
