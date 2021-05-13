c500 = int(input())
c100 = int(input())
c50 = int(input())
x = int(input())
count = 0
 
for c500_n in range(c500+1):
  for c100_n in range(c100+1):
    for c50_n in range(c50+1):
      if c500_n*500 + c100_n*100 + c50_n*50 == x:
        count += 1
 
print(count)