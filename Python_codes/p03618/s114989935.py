from collections import Counter

n=list(input())
l=len(n)
a=l*(l-1)/2

counter = Counter(n)
for w, c in counter.most_common():
  a -= c*(c-1)/2
print(int(a+1))    