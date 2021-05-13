s=list(input())
n=len(s)
count=0
for i in range(n):
    if i%2==0:
        if s[i]=="p":
            count-=1
    else:
        if s[i]=="g":
            count+=1
print(count)