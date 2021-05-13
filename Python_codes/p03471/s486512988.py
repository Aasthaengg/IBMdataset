n , y = map(int, input().split())

i = y//10000
j = y//5000
k = y//1000

for p in range(i+1):
  for q in range(j+1):
    if (n-p-q)>=0 and (p*10000)+(q*5000)+((n-p-q)*1000)==y:
      print(p, q, n-p-q)
      exit()
    
print(-1, -1, -1)