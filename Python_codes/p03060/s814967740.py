n=int(input());v=list(map(int,input().split()));c=list(map(int,input().split()))
print(sum([i-j for i,j in zip(v,c) if i>j]))