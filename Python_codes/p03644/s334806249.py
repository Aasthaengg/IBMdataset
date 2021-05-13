x = [2 ** i for i in range(20)]
N = int(input())
for j in range(len(x)):
  if x[j] <= N < x[j + 1]:
    print(x[j])
    break
    
