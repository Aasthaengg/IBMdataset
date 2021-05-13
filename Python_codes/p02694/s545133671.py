x= int(input())
eq=100
cont=0
while x > eq:
    eq= eq+(eq*1)//100
    cont+=1
print(cont)