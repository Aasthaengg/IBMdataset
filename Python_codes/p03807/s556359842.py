n=int(input())
a=list(map(int,input().split()))
m=0
ans=['YES','NO']
for i in a:
  m+=i%2
print(ans[m%2])