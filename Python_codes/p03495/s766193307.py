N,K=map(int,input().split())
A=list(map(int,input().split()))
count = [0]*max(A)
for i in A:
  count[i-1] += 1
print(sum(sorted(count,reverse=True)[K:]))