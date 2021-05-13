n=int(input())
l=list(map(int, input().split()))
#l=list(l)
count=0
for i in range(n-2):
    for j in range(i+1,n-1):
        #print(i)
        if l[j]!=l[i]:
            #print(i)
            for k in range(j+1,n):
                a,b,c=[l[i],l[j],l[k]]
                if a!=c and b!=c:
                    if a+b>c and b+c>a and c+a>b:
                        count+=1
                    #print(i+1,j+1,k+1)
print(count)