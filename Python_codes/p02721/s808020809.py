n,k,c=[int(x) for x in input().split()]
s=list(input())

L=[]
R=[]

i=0
while i < n:  
    if s[i]=="o":
        L.append(i)
        i+=c
    i+=1

i=0
while i < n:
    if s[n-i-1]=="o":
        R.append(n-i-1)
        i+=c
    i+=1
    
days=[]
for i in range(k):
    if L[i]==R[k-i-1]:
        days.append(L[i])


for i in range(len(days)):
    print(days[i]+1)