a, b = map(int, input().split())

ans = 0

for i in range(1,10):
  for j in range(0,10):
    for k in range(0,10):
      num = [str(i),str(j),str(k),str(j),str(i)]
      
      if int(''.join(num)) >= a and int(''.join(num)) <= b:
#        print(num)
        ans += 1
        
print(ans)