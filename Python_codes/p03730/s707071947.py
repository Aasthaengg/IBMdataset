A,B,C = map(int,input().split())

for n in range(1,100):
  if A*n%B == C:
    print("YES")
    exit()

print("NO")