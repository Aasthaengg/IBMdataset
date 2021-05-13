import itertools

n = int(input())
d = [int(num) for num in input().split()]

d.sort(reverse=True)

result = []
for conb in itertools.combinations(d, 2):
  result.append(list(conb)) 
  
answer = 0
for i in result:
  answer += i[0]*i[1]

print(answer)