n = int(input())
lis = list(map(int,input().split()))
lis[0]-=1
for i in range(n-1):
  if lis[i] < lis[i+1]:
    lis[i+1] -= 1
  elif lis[i] > lis[i+1]:
    print("No")
    exit()
print("Yes")
