s = set(list(input()))
n = set(list(map(chr,list(range(97,97+26)))))
print('None' if len(s)==len(n) else min(n-s))