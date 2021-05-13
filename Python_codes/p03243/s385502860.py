n=input()
s=int(n)
for i in range(s,1000):
    if(len(set(str(i)))==1):
        print(i)
        exit()
