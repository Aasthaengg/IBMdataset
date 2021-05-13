x=int(input())
num1=(x//11)*2
num2=x%11
if num2>=7:
    num1+=2
elif num2!=0:
    num1+=1
print(num1)
