N,K = list(map(int,input().split()))
H  = list(map(int,input().split()))
counter = 0
for h in H:
  if h >= K:
    counter += 1
    
print(counter)
