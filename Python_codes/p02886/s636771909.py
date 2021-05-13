N = int(input())
a = input().split()

sum = 0

for i in range(N-1):
  for j in range(i+1,N):
    #print(int(a[i])*int(a[j]))
    sum += int(a[i])*int(a[j])
  
print(sum)