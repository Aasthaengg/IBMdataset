def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

a,b,k = iim()

for i in range(k):
    if i%2 == 0:
        if a%2 == 1:
            a -= 1
        a = a//2
        b += a
    else:
        if b%2 == 1:
            b -= 1
        b = b//2
        a += b

print(a,b)