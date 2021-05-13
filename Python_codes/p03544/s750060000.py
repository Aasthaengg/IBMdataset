memo = {0:2, 1:1}

n = int(input())

for number in range(2,n+1):
  memo[number] = memo[number-1] +  memo[number-2]
  
print(memo[n])