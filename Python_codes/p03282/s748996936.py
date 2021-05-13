S=str(input())
K=int(input())

first_number=1
location=0
for i in range(len(S)):
  if int(S[i]) != 1:
    first_number = S[i]
    location = i
    break
if K <= location:
  print(1)
else:
  print(first_number)