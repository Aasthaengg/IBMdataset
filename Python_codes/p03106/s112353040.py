a, b, k =map(int,input().split())
t =[]
for i in range(1,max(a,b)+1):
  if a % i == b % i == 0:
    t.append(i)
print(t[-k])