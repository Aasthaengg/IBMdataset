import collections
alpha=['a','b','c','d','e','f','g','h','i','j']
def a(n):
  if n==1:
    return ['a']
  else:
    box=[]
    alphan=alpha[:n+1]
    for i in a(n-1):
      kind=collections.Counter(i)
      for j in range(len(kind)+1):
        box.append(i+alpha[j])
  return box
for i in a(int(input())):
  print(i)