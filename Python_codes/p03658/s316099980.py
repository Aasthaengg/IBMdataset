def calclength(N, K, length) :
  length.sort(reverse = True)
  lengthsum = 0
  for i in range(K) : 
    lengthsum += length[i]
    
  return lengthsum

N, K = tuple(map(int, input().split()))

length = list(map(int, input().split()))

print(calclength(N, K, length))
