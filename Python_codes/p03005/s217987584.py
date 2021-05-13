line = input().split()
N = int(line[0])
K = int(line[1])
 
if K==1:
  ans = 0
else:
  ans = N-K
print(ans)