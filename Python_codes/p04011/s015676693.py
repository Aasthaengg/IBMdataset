a=int(input())
b=int(input())
c=int(input())
d=int(input())
sum=0
for i in range(a):
    if i<=b-1:
        sum+=c
    else:
        sum+=d
print(sum)