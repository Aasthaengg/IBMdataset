

def intinput():
    return int(input())

def listintinput():
    return list(map(int,input().split()))

def splitintinput():
    return map(int,input().split())

N = intinput()
ans = 0
for i in range(N):
    a,b = splitintinput()
    ans += b-a+1

print(ans)

