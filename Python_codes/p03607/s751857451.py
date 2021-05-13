n=int(input())
a=[int(input()) for i in range(n)]
num={}
counter=0
for i in range(n):
    num.setdefault(a[i],0)
    num[a[i]]+=1

for i in num:
    if num[i]%2!=0:
        counter+=1

print(counter)
