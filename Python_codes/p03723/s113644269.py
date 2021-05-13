A,B,C = map(int, input().split())

count = 0
while(A%2==0 and B%2==0 and C%2==0):
  if A==B==C:
    count = -1
    break
    
  tot = A+B+C
  A = (tot-A)/2
  B = (tot-B)/2
  C = (tot-C)/2
  count+=1

print(count)