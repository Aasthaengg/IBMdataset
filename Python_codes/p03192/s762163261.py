n=input()
N=list(n)
count=0
for i in range(4):
    if N[i]=='2':
        count+=1
print(count)