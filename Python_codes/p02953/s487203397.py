n = int(input())
h = list(map(int, input().split()))
Flag = "Yes"
maxh = 0

if n >= 2 :
  for i in range(1,n):
    if h[i-1] > h[i]:
      h[i-1] = h[i-1] - 1
      if h[i-1] > maxh:
        maxh = h[i-1] 
      if h[i-1] > h[i] or maxh > h[i] :
        Flag = "No"
      
print(Flag)