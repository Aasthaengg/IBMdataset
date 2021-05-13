n,l=map(int,input().split())
ringo=[i+l-1 for i in range(1,n+1)]
ringo.sort(key=lambda x:abs(x))
print(sum(ringo[1:]))