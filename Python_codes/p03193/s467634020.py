N, H, W = map(int, input().split())
cnt = 0
l=[]

while cnt <= N-1:
  _ = [i for i in map(int, input().split())]
  if H <= _[0] and W <= _[1]:
  	l.append(_)
  cnt += 1
  
print(len(l))