l=list(map(int,input().split()))
a=max(l)*3-sum(l)+1
print(a//2 if a%2 else a//2+1)