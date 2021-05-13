##### 解けた #####

a,b,c=list(map(int,input().split(" ")))
sumabc=(a+b+c)

print(sumabc-max(a,b,c))