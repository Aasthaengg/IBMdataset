import re
print(max([0]+[len(r) for r in re.findall("[ACGT]+",input())]))