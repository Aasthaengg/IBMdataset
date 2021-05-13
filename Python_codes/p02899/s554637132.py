N=int(input())
A=list(map(int,input().split()))

pairs = list(zip(range(1,N+1),A))
pairs = sorted(pairs, key=lambda x:x[1])
print(*(list(zip(*pairs))[0]))