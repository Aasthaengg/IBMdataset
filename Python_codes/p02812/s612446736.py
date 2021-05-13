n=int(input())
s=input()
l=[]
count=0
for i in s:
    if i=='A':
        l=['A']
    elif i=='B' and l==['A']:
        l.append('B')
    elif i=='C' and l==['A','B']:
        l=[]
        count+=1
    else:
        l=[]
print(count)