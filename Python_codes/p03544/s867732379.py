#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]
#a = [int(input()) for _ in range(n)]


n = int(input())

if (n == 1):
    print(1)
else:
    l1 = 2
    l2 = 1
    ans = 0
    for i in range(n-1):
        ans = l2 + l1
        l1 = l2
        l2 = ans
    print(ans)


