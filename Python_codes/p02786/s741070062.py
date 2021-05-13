H = int(input())
count = 0
while H > 1:
  H = H // 2
  count += 1
print(2**(count+1)-1)