#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]
#a = [int(input()) for _ in range(n)]

a,b,x=map(int, input().split())

if ( 0 <= (x-a) and (x-a) <= b ):
    print("YES")
else:
    print("NO")




