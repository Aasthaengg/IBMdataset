#input
N = int(input())

count=0
for i in range(1,int(N/2)+1):
#  print(i)
  #if(N-i == 0):
  count += 1

if(N%2 == 0):
  count -= 1

#output
print(count)