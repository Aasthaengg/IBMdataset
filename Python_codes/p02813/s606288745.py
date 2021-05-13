import itertools

N = int(input())
P = tuple([ int(v) for v in input().split(" ") ])
Q = tuple([ int(v) for v in input().split(" ") ])

p_list = list(itertools.permutations(range(1, N+1), N))

a = 0
b = 0
for i in range(len(p_list)):
  if p_list[i] == P:
    a = i+1
  if p_list[i] == Q:
    b = i+1

#print(a,b)
print(abs(a-b))
