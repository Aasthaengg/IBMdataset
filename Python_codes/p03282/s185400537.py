s=input()
k=int(input())

ts=s[:k]
if ts.count('1')==len(ts):
  print(1)
  exit()

for i in s:
  if i!='1':
    print(i)
    exit()