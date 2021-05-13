n=int(input())
s=input()
se=[set() for _ in range(3)]
for a in s:
  for pre in se[1]:
    se[2].add(a+pre)
  for pre in se[0]:
    se[1].add(a+pre)
  se[0].add(a)
print(len(se[2]))
