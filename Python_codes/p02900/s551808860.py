A, B = map(int, input().split())

def fact(n):
    k = 2
    l = [] 
    temp=n
    while pow(k, 2)<=n:
        if temp%k==0:
            l.append(k)
            while temp%k==0:
                temp//=k
        k+=1
    if temp!=1:
        l.append(temp)
    return l

if A==1 and B==1:
    print(1)
elif A==B:
    print(len(set(fact(A)))+1)
else:
    print(len(set(fact(A))&set(fact(B)))+1)