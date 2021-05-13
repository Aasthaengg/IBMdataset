N = int(input())
A, B = map(int, input().split())
P = [int(i) for i in input().split()]

ret = [0] * 3
for p in P :
  if p <= A :
    ret[0] += 1
  elif A + 1 <= p <= B :
    ret[1] += 1
  else :
    ret[2] += 1
    
print(min(ret))