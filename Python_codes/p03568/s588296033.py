n = int(input())
A = list(map(int,input().split()))

even = odd = 0

for a in A:
  if a%2:
    odd += 1
  else:
    even += 1
    
print(3**n - 2**even)

