A,B,C =  map(int,input().split())
count = 0
for _ in range(A):
  D,E = map(int,input().split())
  if B <= D  and C <=  E:
    count += 1
print(count)