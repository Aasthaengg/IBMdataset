n=input();l=[int(x) for x in n]
for i in range(min(set(l)),max(set(l))+1):
  ans=int(str(i)*3)
  if ans>=int(n):
    print(ans)
    break