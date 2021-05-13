n = int(input())
lst1 = list(map(int,input().split()))

def func(a,b):
    for i in range(21):
        if (a>>i)&(b>>i): #AND回路
            return False
    return True

def add_point(length):
    res = 0
    for i in range(1,length):
        res += i
    return res

a,b,count,ans = 0,1,0,0
host = lst1[0]
#尺取法
while True:
    if b >= n and a >= n:
        break
    while  b<n and func(host,lst1[b]):
        host = host^lst1[b]
        b += 1
    host = host^lst1[a] #使わなくなる部分を引く
    if b -a > 1:
        ans += b-a-1
    a += 1

ans += n
print(ans)