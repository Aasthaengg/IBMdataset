a = list(input())
done = False
for s in list('abcdefghijklmnopqrstuvwxyz'):
  if a.count(s) == 0 and not done:
    print(s)
    done = True

if not done:
  print("None")