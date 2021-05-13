a=input().split(" ")

number1=int(a[0])
number2=int(a[1])
n1=0
n2=0

for i in range(number1+1):
    for j in range(number1+1):
        n1=number2-int(i)-int(j)
        if n1<=number1 and 0<=n1:
            n2=n2+1

print(n2)
