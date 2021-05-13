s = input()

s_list = list(s)

from collections import Counter

counter = Counter(s_list)

times = len(s_list)

half = times // 2
print(min(counter["g"] - half, half-counter["p"]))

