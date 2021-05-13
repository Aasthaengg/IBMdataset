import sys

n = int(sys.stdin.readline().rstrip())
a = [int(x) for x in sys.stdin.readline().rstrip().split()]

a_set = set()
counter_wild = 0
for x in a:
    if x>=3200:
        counter_wild+=1
    else:
        a_set.add(x//400)
print(max(1,len(a_set)),len(a_set)+counter_wild)
