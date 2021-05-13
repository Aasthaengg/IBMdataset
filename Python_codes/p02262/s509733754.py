counter=0

def insert(lst,n,g):
    for i in range(g,n):
        v=lst[i]
        j=i-g
        global counter
        while j>=0 and lst[j]>v:
            lst[j+g]=lst[j]
            j=j-g
            counter+=1
        lst[j+g]=v

n=int(input())
lst=[int(input()) for _ in range(n)]
work=n//4
glst=[]
while work>=0:
    glst.append(work+1)
    if work==0 : break
    work//=4

m=len(glst)
for i in range(m):
    insert(lst,n,glst[i])

print(m)
print(" ".join(map(str,glst)))
print(counter)
for i in range(n): print(lst[i])

