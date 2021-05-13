#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]


x1,y1,x2,y2 = map(int, input().split())

dis_x = x2 - x1
dis_y = y2 - y1

x3 = x2 - dis_y
y3 = y2 + dis_x
x4 = x3 - dis_x
y4 = y3 - dis_y

print(x3,y3,x4,y4)


