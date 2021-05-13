#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

n = int(input())
k = int(input())
x = int(input())
y = int(input())

temp = n - k

if (temp >= 0):
    print(x*k + temp*y)
else:
    print(x*n)

