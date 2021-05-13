import re
S = input()
T = re.findall(r'[ATGC]*', S)
print(len(max(T, key=len)))