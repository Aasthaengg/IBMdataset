ais = map(int, raw_input().split()) #1 6 3
ais.sort()
print sum([v-  u for u,v in zip(ais, ais[1:])])