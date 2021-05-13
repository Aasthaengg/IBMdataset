n=int(input())
a = list(map(int,input().split()))
count =1
 
while all(a[i]%(2**count)==0 for i in range(n)):
  count+=1
print(count-1)