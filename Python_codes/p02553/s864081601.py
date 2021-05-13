a,b,c,d = map(int,input().split())

val1 = a*c
val2 = a*d
val3 = b*c
val4 = b*d
print(max(val1,val2,val3,val4))