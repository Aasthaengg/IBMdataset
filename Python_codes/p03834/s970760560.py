#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

s = input()

for i in range(19):
    if (i==5 or i==13):
        print(" ", end="")
    else:
        print(s[i], end="")


