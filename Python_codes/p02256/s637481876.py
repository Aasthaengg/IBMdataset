# coding: utf-8
# Here your code !
def mcg(a,b):
    if a==b:
        return a
    else:
        
        while a%b !=0:
            x = a%b
            a = b
            b = x
        return x

num =sorted(list(map(int,input().split(" "))))
print(mcg(num[0],num[1]))