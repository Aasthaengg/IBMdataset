n=int(input())
d=dict()
for i in range(n):
    a=input()
    if a in d:
        d[a]=(d[a]+1)%2
    else:
        d[a]=1
print(len([i for i,j in d.items() if j==1]))
#print(d.items())