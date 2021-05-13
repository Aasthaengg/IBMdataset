N = int(input())
mochi = []
for i in range(N):
  a = int(input())
  if not a in mochi:
    mochi.append(a)
    
mochi.sort()
print(len(mochi))
