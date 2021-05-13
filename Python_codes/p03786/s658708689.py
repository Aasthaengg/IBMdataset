N = list(map(int,input().split()))
A = [(a,idx+1) for idx,a in enumerate(list(map(int,input().split())))]
A = sorted(A)

color_set = set()
prev_sum = 0
prev_num = 0
for a,color in A:
  if prev_num == a or prev_sum*2 >=a :
    color_set |= {color}
  else:
    color_set = {color}
  prev_sum += a
  prev_num = a
  
print(len(color_set))