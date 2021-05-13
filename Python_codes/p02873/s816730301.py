import re
print(sum(sum(i * (i - 1) // 2 for i in p) + max(p) for p in (tuple(map(len, m)) for m in re.findall(r"(<*)(>*)", input()))))