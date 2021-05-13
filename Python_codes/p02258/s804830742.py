n = input()
n_max = -(10**9)
n_min = input() 

for i in range(0, n-1):
 R = input()
 if n_max < R - n_min:
  n_max = R - n_min
 if R < n_min:
  n_min = R
 
print n_max