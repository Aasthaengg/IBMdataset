from collections import Counter

sc=Counter(input())
tc=Counter(input())

for s,t in zip(sorted(sc.values()),sorted(tc.values())):
    if s!=t:
      print("No")
      break
else:
    print("Yes")