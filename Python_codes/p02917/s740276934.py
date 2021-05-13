n=int(input());b=list(map(int,input().split()))
print(sum([b[0]]+[min(b[i-1],b[i]) for i in range(1,n-1)]+[b[-1]]))