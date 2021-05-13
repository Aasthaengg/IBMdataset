n = int(input())
a = list(map(int,input().split()))
imos = 0
ruisekiwa = [0 for _ in range(n)]
ruisekiwa[0] = a[0]
for i in range(1, n):
	ruisekiwa[i] = ruisekiwa[i-1] + a[i]

# minus
imos = 0
minusans = 0
for i in range(n):
	targ = ruisekiwa[i] + imos
	if i % 2 == 0:
		if targ >= 0:
			imos -= targ+1
			minusans += targ+1
	else:
		if targ <= 0:
			imos += 1-targ
			minusans += 1-targ

# plus
imos = 0
plusans = 0
for i in range(n):
	targ = ruisekiwa[i] + imos
	if i % 2 == 1:
		if targ >= 0:
			imos -= targ+1
			plusans += targ+1
	else:
		if targ <= 0:
			imos += 1-targ
			plusans += 1-targ

print(min(minusans, plusans))