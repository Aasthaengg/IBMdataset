N=input()

num=list(N)
sum=0;
for i in range(1 << len(num)-1):
    l=[]
    for j in range(len(num)):
        l+=num[j]
        if (j != len(num)-1):
            if (i & (1<<j)):
                l+=['+']
        
    sum+=eval("".join(l))
print(sum)
