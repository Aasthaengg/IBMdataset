#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]
#a = [int(input()) for _ in range(n)]

a,b,c = map(int, input().split())

c1 = abs(a-b)
c2 = abs(a-c)
c3 = abs(c-b)

print(c1+c2+c3-max(c1,c2,c3))

