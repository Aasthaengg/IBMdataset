N = input()
Num = sum(pow(10,x)-pow(10,x-1) for x in range(0,len(N)) if x%2)
if len(N)%2:
    print(Num+int(N)-pow(10,len(N)-1)+1)
else:
    print(Num)