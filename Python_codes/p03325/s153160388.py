N = int(input())
a = list(map(int,input().split()))

def count_2(n):
  cnt = 0
  while n % 2 == 0:
    n //= 2
    cnt += 1
  return cnt

A =[0]

for i in a:
  A.append(count_2(i))
  
print(sum(A))  