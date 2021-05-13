s=str(input())
n=int(input())
for i in range(n):
    a=list(input().split())
    x=int(a[1])
    y=int(a[2])
    if a[0]=="print":
        print(s[x:y+1])
    elif a[0]=="replace":
        c=a[3]
        s=s[0:x]+c+s[y+1:]
    elif a[0]=="reverse":
        s=s[:x]+s[x:y+1][::-1]+s[y+1:]
        
