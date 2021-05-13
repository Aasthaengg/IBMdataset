k= int(input())
a, b= input().split()
a= int(a)
b= int(b)
cont=0
while 1:
    cont+= k
    if a<= cont <= b:
        print("OK")
        break
    if cont > b:
        print("NG")
        break