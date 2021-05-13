n=int(input())
num=[]
def ap(num1):
    num.append(num1)
for i in range(n):
    ap(list(map(int,input().split())))
num2=0
str1= lambda val: val[1]
num.sort(key=str1)
ans=0
for i in range(n):
    num2+=num[i][0]
    if num2>num[i][1]:
        ans=1
        break
if ans==1:
    print("No")
else:
    print("Yes")
