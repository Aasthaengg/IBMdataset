import re
print(max(len(i) for i in re.sub(r'[^ACGT]', '_', input()).split('_')))