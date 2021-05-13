x,n = map(int,input().split())
if n == 0:
  print(x)
  exit()
nums = list(map(int,input().split()))
cnt =0
while True:
  if x-cnt not in nums:
    print(x-cnt)
    break
  if x+cnt not in nums:
    print(x+cnt)
    break
  cnt +=1
