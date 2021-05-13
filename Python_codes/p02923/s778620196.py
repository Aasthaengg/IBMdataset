n=int(input())
l = list(map(int,input().split()))
max=0
a=0
for i in range(n-1):
    if l[i+1]<=l[i]:
        a+=1
        if a>=max:
            max=a
    elif l[i+1]>l[i]:
        if a>=max:
            max=a
        a=0
print(max)