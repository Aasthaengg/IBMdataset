k=input()

list_a=k.split()

n=list_a[0]

m=list_a[1]

t=input()

list_b=t.split()

h=len(list_b)

list_s=[int(s) for s in list_b]

if int(m)==int(h) and sum(list_s) <= int(n):
  print(int(n)-sum(list_s))
elif int(m)==int(h) and sum(list_s) > int(n):
  print("-1")
