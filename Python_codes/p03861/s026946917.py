a,b,x = list(map(int,input().split()))
a1 = a//x if a%x else a//x-1
a2 = b//x
print(a2-a1)