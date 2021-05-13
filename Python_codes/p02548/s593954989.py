N = int(input())
count_eq = 0
count_df = 0
for i in range(1,N):
  for j in range(i,N):
    if i*j <= N-1:
      if i == j:
        count_eq += 1
      else :
      	count_df += 1
    else :
      break
print(count_eq + 2*count_df)