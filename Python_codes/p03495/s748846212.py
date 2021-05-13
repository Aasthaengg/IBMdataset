def ra(a): #圧縮された要素を非保持
    ll,l=[],1
    for i in range(len(a)-1):
        if a[i]==a[i+1]:
            l+=1
        else:
            ll.append(l)
            l=1
    ll.append(l)
    return ll
n,k=map(int,input().split())
a=list(map(int,input().split()))
b=sorted(ra(sorted(a)))
print(sum(b)-sum(b[-k:]))