l=list(map(int,input().split()))
mid=sum(l)-max(l)-min(l)
print(sum(l)-mid*2)