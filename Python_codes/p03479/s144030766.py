X,Y=map(int,input().split())
count=1
old=X
new=X
while 1:
  new += old
  if new > Y:break
  count += 1
  old = new

print(count)