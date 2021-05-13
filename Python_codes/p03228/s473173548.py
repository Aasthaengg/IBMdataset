a,b,k = map(int, input().split())
flag = 0
for i in range(k):
    if flag == 0:
        if a%2 == 1: a-= 1
        b += a//2
        a -= a//2
    if flag == 1:
     if b%2 == 1:b-= 1
     a += b//2
     b -= b//2
    if flag == 0: flag =1
    else:flag =0
print(a,b)
