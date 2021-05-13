s = set(input())
al = set(list(map(chr, [i for i in range(97, 97+26)])))
print('None' if len(s)==len(al) else min(al-s))
