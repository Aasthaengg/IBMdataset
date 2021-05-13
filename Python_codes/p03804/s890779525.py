n,m = map(int, input().split())
a = [input() for _ in range(n)]

for _ in range(m):
  b = input()
  for i in a:
    if i.find(b) >= 0: break
    print("No")
    exit()
    
print("Yes")