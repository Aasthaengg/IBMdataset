from itertools import permutations

N = int(input())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))

nums =[i for i in range(1,N+1)]
pers =permutations(nums,N)
count = 0
for i in pers:
  count += 1
  if P == list(i):
    a = count
  if Q == list(i):
    b = count

print(abs(a-b))