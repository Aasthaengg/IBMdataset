n = int(input())
hn = [int(num) for num in input().split()]

for i in range(n-1,0,-1):
  if hn[i-1] > hn[i]:
    hn[i-1] -= 1
    if hn[i-1] > hn[i]:
      print("No")
      exit()
            
print("Yes")