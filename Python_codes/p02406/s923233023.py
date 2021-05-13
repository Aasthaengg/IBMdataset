N=int(input())
count = ""
for i in range(1,N+1):
 x=i
 if x%3==0:
  count += " " + str(i)
 else:
   while x:
      if x % 10 == 3:
          count += " " + str(i)
          break
      x //= 10
print(count)