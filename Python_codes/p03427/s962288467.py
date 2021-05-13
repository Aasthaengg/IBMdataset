n=input()
c=0
for i in range(1,int(len(n))):
    if n[i]=="9":
        c+=1
if c==len(n)-1:
    print(int(n[0])+9*(len(n)-1))
else:
    print(int(n[0])+9*(len(n)-1)-1)