n = int(input())
city = []
nums = []
result = []
 
for i in range(n):
  s,p = input().split()
  p = int(p)
  city.append(s)
  nums.append(p)
  result.append([s,p,i+1])
 
for i in sorted(set(city)):
  for j in sorted(set(nums), reverse = True):
    for k in result:
      if k[0] == i and k[1] == j:
        print(k[2])