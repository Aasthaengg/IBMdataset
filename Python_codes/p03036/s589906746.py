#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

r,D,x2000 = map(int, input().split())

x = x2000
for i in range(10):
    ans = r*x - D
    print(ans)
    x = ans
