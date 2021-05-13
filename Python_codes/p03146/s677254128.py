n=int(input())
l=[n]

i=1
while len(set(l))==i:
    if n%2==0:
        n=n/2
    else:
        n=3*n+1
    l.append(n)
    i+=1
print(i)