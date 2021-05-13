k = int(input())
a, b = map(int, input().split())
count = 0
 
for i in range(b-a+1):
  if (a + i) % k == 0:
    count += 1
  
print("OK" if count > 0 else "NG")