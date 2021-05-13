x=int(input())
a=(x//11)*2
print(a if x%11==0 else a+1 if x%11<7 else a+2)