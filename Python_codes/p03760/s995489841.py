#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]

o = input()
n = input()

for i in range(len(n)):
    print(o[i], end="")
    print(n[i], end="")

if len(o) - len(n) == 1:
    print(o[-1])

