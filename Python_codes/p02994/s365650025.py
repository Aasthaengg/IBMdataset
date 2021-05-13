n,l=map(int,input().split())
li=[l+i for i in range(n)]
print(sum(li)-sorted(li,key=lambda x:abs(x))[0])