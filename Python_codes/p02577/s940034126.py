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

n = inp()
m = int(n)

ans = 0

for i in range(len(n)):
    ans += int(n[i])

ans %= 9

if ans == 0:
    print("Yes")
else:
    print("No")