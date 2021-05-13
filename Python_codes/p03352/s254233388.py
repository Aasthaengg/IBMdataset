n = int(input())
maxi = 1
for i in range(1,32):
  for j in range(2,10):
    l = i**j
    if l<=n:
    	maxi = max(maxi, l)
print(maxi)