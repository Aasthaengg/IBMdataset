n,k=map(int,input().split())
s=input()
count=0
result=''
for i in s:
    count+=1
    if count==k:
        S=i.lower()
        result+=S
    else:
        result+=i
print(result)