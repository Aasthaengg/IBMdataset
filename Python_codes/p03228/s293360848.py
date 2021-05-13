a,b,k=map(int,input().split())

for i in range(0,k):
    if i%2!=0:
        a+=b//2
        b = b // 2
    else:
        b += a // 2
        a = a // 2

ans=[a,b]
print(" ".join(map(str,ans)))