s=list(input())
t=list(input())
s.sort()
t.sort(reverse=True)
a=[s,t]
a.sort()
if s==t:
  print("No")
else:
  if a[0]==s:
    print("Yes")
  else:
    print("No")