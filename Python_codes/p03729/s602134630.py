#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]


a,b,c = map(str, input().split())

if (a[-1] == b[0] and b[-1] == c[0]):
    print("YES")
else:
    print("NO")
