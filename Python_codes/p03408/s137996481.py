from collections import Counter
N = int(input())#blue card +
s = list(input() for i in range(N))
M = int(input())#red card -
t = list(input() for i in range(M))
count_p = Counter(s)
count_m = Counter(t)
counter = count_p - count_m
if (len(counter.values()) == 0):
    print (0)
else:
    print(max(counter.values()))