def maximumx(N, S) : 
  x = 0
  max = 0
  
  for i in range(N) : 
    if S[i] == 'I' : 
      x += 1
      if max < x :
        max = x
    else : 
      x -= 1 
      
  return max


N = int(input())
S = input()

print(maximumx(N, S))