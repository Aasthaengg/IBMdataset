s = input()
months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
if s[:2] in months and s[2:] in months:
	print("AMBIGUOUS")
elif s[:2] in months and s[2:] not in months:
	print("MMYY")
elif s[:2] not in months and s[2:] in months:
	print("YYMM")
else:
	print("NA")