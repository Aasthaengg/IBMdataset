N=int(input())

a=N//11
b=N%11


count=0
count+=2*a
if 0<b and b<=6:
    count+=1
elif 6<b:
    count+=2

print(count)