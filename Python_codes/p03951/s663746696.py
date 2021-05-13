def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
s = list(input())
t = list(input())

for i in range(n):
    if s[i:] == t[:n-i]:
        print(n+i)
        exit()


print(2*n)