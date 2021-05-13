N = int(input())
A = list(map(int,input().split()))
 
cnt = 0
while True:
  check = sum([n % 2 for n in A])
  if check == 0:
    A = [n/2 for n in A]
    cnt += 1
  else:
    break
    
print(cnt)