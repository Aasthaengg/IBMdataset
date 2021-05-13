N, K = map(int,input().split())
H = list(map(int,input().split()))

hum = 0

for h in H:
  if K <= h:
    hum += 1
    
print(hum)