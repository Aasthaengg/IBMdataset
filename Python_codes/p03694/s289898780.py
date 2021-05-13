def coordminmax(N) : 
  coordinate = list(map(int, input().split()))
  min = coordinate[0]
  max = coordinate[0]
  
  for i in range(len(coordinate)) : 
    if coordinate[i] < min : 
      min = coordinate[i]
      
    if coordinate[i] > max : 
      max = coordinate[i]
      
  return min, max

def calcdistance(N) : 
  min, max = coordminmax(N)
  return max - min


N = int(input())

print(calcdistance(N))