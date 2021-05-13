#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]
#a = [int(input()) for _ in range(n)]

n = int(input())

l = []
for i in range(100//4):
    for j in range(100//7):
        l.append(i*4+j*7)
if n in l:
    print("Yes")
else:
    print("No")



