N = int(input())
count = 0
for i in range(1,N+1):
  if i<10 or 100<=i<1000 or 10000<=i<100000:
    count += 1
    
print(count)