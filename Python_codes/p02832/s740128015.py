N=int(input())
A=list(map(int,input().split()))

cnt=0
for a in A:
  cnt+=1 if cnt+1==a else 0
print(N-cnt if cnt>0 else -1)