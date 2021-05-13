num=int(input().rstrip())
m=input().rstrip().split()
main=[]
for i in m:
    main.append(int(i))
sample=sorted(main,reverse=True)
result=0
for i in range(2,num+1):
    if i%2==0:
        y=i/2-1
        result+=sample[int(y)]
    else:
        y=(i+1)/2-1
        result+=sample[int(y)]
print(result)
