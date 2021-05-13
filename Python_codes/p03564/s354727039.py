a=int(input())
b=int(input())
val=1
for i in range(a):
    if 2*val>=val+b:
        val+=b
    else:
        val*=2
print(val)