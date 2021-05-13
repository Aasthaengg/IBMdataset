ans=[]
N=int(input())
alf=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

while N>0:
    N,b=divmod(N-1,26)
    b=alf[b]
    ans.insert(0,b)


print(''.join(ans))
