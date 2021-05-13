n = int(input())
an = [int(num) for num in input().split()]
bn = [int(num) for num in input().split()]
cn = [int(num) for num in input().split()]

sum = 0
for a in an:
  sum += bn[a-1]

add = []
for i in range(n-1):
  if an[i]+1 == an[i+1] :
    add.append(an[i])

for j in add:
  sum += cn[j-1]
    
print(sum)