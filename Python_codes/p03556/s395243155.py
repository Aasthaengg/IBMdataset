n = int(input())
answer = 1
while True:
  if answer**2 > n:
    print((answer-1)**2)
    break
  answer+=1