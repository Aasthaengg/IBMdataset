k = int(input())
x = 7%k
s = set()
#i = 1
#while len(s) == 0:
for i in range(1, k+1):
  if x == 0:
    print(i)
    exit()
  #s.add(x)
  x = (x*10+7)%k
  #i += 1
print(-1)
