a,b,c=map(int,input().split())
k=int(input())

l=[a,b,c]
l=sorted(l,reverse=True)

print(l[0]*(2**k)+l[1]+l[2])

