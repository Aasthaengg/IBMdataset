n = raw_input()
ais = map(int , raw_input().split())
i = 0
j = 0
cumul = 0
r = 0
while(i < len(ais)):
	while(j < len(ais) and (cumul & ais[j] == 0)):
		cumul |= ais[j]
		j += 1
	r += j - i
	cumul ^= ais[i]
	i += 1
print r