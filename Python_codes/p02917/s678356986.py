n = int(input())
B = list(map(int,input().split()))

sum = B[0] + B[-1]

for i in range(len(B)-1):
  sum += min(B[i],B[i+1])
  
print(sum)

