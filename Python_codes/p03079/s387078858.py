def trya(a):
  if sum(a)==3*a[0]:
    return "Yes"
  else:
    return "No"

a=list(map(int,input().split()))
print(trya(a))