def inp():
    return input()
def iinp():
    return int(input())
def inps():
    return input().split()
def miinps():
    return map(int,input().split())
def linps():
    return list(input().split())
def lmiinps():
    return list(map(int,input().split()))
def lmiinpsf(n):
    return [list(map(int,input().split()))for _ in range(n)]

n = iinp()
a = lmiinps()

ans = 0

for i in range(n-1):
    if a[i+1] < a[i]:
        ans += (a[i] - a[i+1])
        a[i+1] = a[i]

print(ans)