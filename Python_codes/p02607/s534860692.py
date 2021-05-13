n=int(input())
arr=list(map(int,input().split()))
ct=0
for _ in range(n):
  if (_+1)%2==1 and arr[_]%2==1:
    ct += 1
print(ct)