N, A, B = map(int,input().split())
#print(N,A,B)


#print(length_N)

count = 0
for i in range(1,N+1):
  total = 0
  string_N = list(str(i))
  length_N = len(str(i))
  
  for j in range(length_N):
    total += int(string_N[j])
  if total >= A and total <= B:
    count += i

print(count)