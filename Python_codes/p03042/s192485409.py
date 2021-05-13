S=input()
first = S[:2]
second= S[2:]
ans=""


if int(first) > 12 or int(first) == 0:#MM
	if int(second) <= 12 and int(second) >= 1:#YY
		ans="YYMM"
	if int(second) > 12 or int(second) == 0:#YY
		ans="NA"

elif int(first) <= 12 and int(first) >= 1:#YY
	if int(second) <= 12 and int(second) >= 1:#YY
		ans="AMBIGUOUS"
	if int(second) > 12 or int(second) == 0:#YY
		ans="MMYY"

print(ans)