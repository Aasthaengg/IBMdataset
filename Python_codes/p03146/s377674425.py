s=int(input())
ss=[s]
n=s
for i in range(2,10**6):
  if n%2==0:
    n=n/2
    if n in ss:
        print(i)
        quit()
    ss.append(n)
  else:
    n=3*n+1
    if n in ss:
        print(i)
        quit()
    ss.append(n)