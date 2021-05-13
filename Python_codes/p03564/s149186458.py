n=int(input())
k=int(input())
start=1
for i in range(n):
  if start<k:
    start=start*2
  else:
    start=start+k
print(start)