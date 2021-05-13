n=int(input())
ans=0.0
for _ in range(n):
  arr = input().split()
  if arr[1]=="JPY":
    ans+=float(arr[0])
  else:
    ans+=float(arr[0])*380000.0

    
print(ans)