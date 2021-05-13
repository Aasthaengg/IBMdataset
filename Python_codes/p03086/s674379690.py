import sys
lines = [s.rstrip("\n") for s in sys.stdin.readlines()]
input = lines.pop(0)
acgt = tuple("ACGT")
max_num_list = []
max_num = 0
for c in input:
    if c in acgt:
        max_num += 1
    else:
        max_num_list.append(max_num)
        max_num = 0
max_num_list.append(max_num)
print(max(max_num_list))
