n=int(input())
a=list(map(int,input().split()))
m=0
for i in a:
  m+=i%2
print(['YES','NO'][m%2])