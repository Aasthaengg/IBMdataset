from collections import deque
s=input()

ds=deque(s)
flag=True

while ds[0]!='A' or ds[-1]!='Z':
  if ds[0]!='A':
    ds.popleft()
  if ds[-1]!='Z':
    ds.pop()
print(len(ds))