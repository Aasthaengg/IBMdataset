l = input()
arr = l.split(' ')
s = set()
if 1 <= int(arr[0]) <= 100 and 1 <= int(arr[1]) <= 100 and 1 <= int(arr[2]) <= 100:
  for e in arr:
    s.add(e)
s = list(s)
print(len(s))