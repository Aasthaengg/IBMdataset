N,M = map(int,input().split())
start = 1
end = M
while True:
  if start>=end:
    break
  print(start,end)
  start+=1
  end-=1
  
start = M+1
end = 2*M+1
while True:
  if start>=end:
    break
  print(start,end)
  start = start+1
  end = end-1