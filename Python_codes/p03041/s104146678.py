#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

n, k = map(int, input().split())
s = input()

for i in range(n):
    if i+1 == k:
        print(s[i].lower(), end="")
    else:
        print(s[i], end="")

