_,*ss = open(0).read().split()

from collections import Counter
c = Counter(ss)

mx = c.most_common(1)[0][1]

for s in sorted(key for key,count in c.items() if count==mx):
    print(s)