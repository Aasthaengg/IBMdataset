N = int(input())
s = list(input())
R_count = s.count("R")
if R_count > N // 2:
	print("Yes")
else:
	print("No")