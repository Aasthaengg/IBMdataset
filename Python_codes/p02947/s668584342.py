n=int(input())
list1=[]
def apl1(l1):
    list1.append(l1)
for i in range(n):
    apl1(str(sorted(list(input()))))
list1.sort()
str1=list1[0]
ans=0
num=0
def num_1(num1):
    return ((num1+1)*num1)//2
for i in range(1,n):
    if str1==list1[i]:
        num+=1
    else:
        ans+=num_1(num)
        str1=list1[i]
        num=0
if num>=1:
    ans+=num_1(num)
print(ans)
