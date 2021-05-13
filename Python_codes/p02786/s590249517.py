h = int(input())
cnt = 1

while(h > 1):
  h = h // 2
  cnt += 1
  
print(2**cnt - 1)