#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]
#a = [int(input()) for _ in range(n)]

n = int(input())
a = list(map(int, input().split()))

ans = 0
while True:
    for i in range(n):
        if (a[i] % 2 != 0):
            print(ans)
            exit()
    for i in range(n):
        a[i] //= 2
    ans += 1

