n = int(input())
ary = list(map(int,input().split()))

cnt = 0
for i in ary:
  if i%2 == 0:
    cnt+=1
    
ans = 3**n - 2**cnt

print(ans)