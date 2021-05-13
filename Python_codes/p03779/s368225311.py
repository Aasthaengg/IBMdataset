d = int(input())
t = 0 
while True:
  if t*(t+1)//2 >=d:
    print(t)
    exit()
  t +=1