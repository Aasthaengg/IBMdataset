#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

a, b, c = map(int, input().split())

ans = 0
if (a != b and a != c and b != c):
    ans = 3
elif (a == b and a == c and b == c):
    ans = 1
else:
    ans = 2
print(ans)

