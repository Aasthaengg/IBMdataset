#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))

a,b = map(int, input().split())


if (b > 9 or a > 9):
    print(-1)
else:
    print(a*b)
