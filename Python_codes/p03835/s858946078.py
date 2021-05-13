#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

k, s = map(int, input().split())

ans = 0
for x in range(k+1):
    for y in range(k+1):
        z = s - (x+y)
        if (z>=0 and z <= k and x+y+z == s):
            #print(x,y,z)
            ans += 1
print(ans)


