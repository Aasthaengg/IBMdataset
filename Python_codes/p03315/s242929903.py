S = list(input())

count = 0
for i in range(4):
  if S[i]=='+':
    count+=1

print(2*count-4)
