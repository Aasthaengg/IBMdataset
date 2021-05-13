import re

letter = str(input())
pattern = 'A(.*)Z'
target = re.search(pattern, letter).group()
print(len(target))