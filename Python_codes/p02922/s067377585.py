A,B = map(int,input().split())
tap = 0
plg = 1

for n in range(20):
  if plg>=B:
    print(tap)
    exit()
  else:
    plg+=A-1
    tap+=1
    
print(tap)