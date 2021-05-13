a=[0]*10**7
a[1]=int(input())
cnt=[a[1]]

def f(v):
  if v%2:
    return 3*v+1
  else:
    return v//2

for i in range(2,10**7+1):
  a[i] = f(a[i-1])
  if a[i] in cnt:
    print(i)
    break
  else:
    cnt.append(a[i])

