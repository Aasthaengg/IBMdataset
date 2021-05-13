#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))

a, b = map(int, input().split())

ans = a - b * 2

if (ans >= 0):
    print(ans)
else:
    print(0)

