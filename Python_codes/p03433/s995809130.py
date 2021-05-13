N = int(input())
A = int(input())
ret = 'No'
for a in range(A+1):
  if N%500==a:
    ret='Yes'
    break
print(ret)
