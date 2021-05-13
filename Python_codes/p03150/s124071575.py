import re
s = input()
a = []
a += [re.match(r'.*keyence$', s)]
a += [re.match(r'k.*eyence$', s)]
a += [re.match(r'ke.*yence$', s)]
a += [re.match(r'key.*ence$', s)]
a += [re.match(r'keye.*nce$', s)]
a += [re.match(r'keyen.*ce$', s)]
a += [re.match(r'keyenc.*e$', s)]
a += [re.match(r'keyence.*$', s)]
print('YES' if any(a) else 'NO')