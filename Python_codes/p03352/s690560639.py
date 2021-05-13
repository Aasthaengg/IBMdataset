#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]
#a = [int(input()) for _ in range(n)]

x = int(input())

ans = 1

for i in range(2,x+1):
    for j in range(2,11):
        if (ans < i ** j):
            if (i**j <= x):
                ans = i ** j
print(ans)




