s = input()
Set = set()
for i in s:
    Set.add(i)
print("yes" if len(Set) == len(s) else "no")