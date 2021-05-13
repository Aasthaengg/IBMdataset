a=int(input())
b=int(input())

l=[0]*3
l[a-1]+=1
l[b-1]+=1
print(l.index(0)+1)
