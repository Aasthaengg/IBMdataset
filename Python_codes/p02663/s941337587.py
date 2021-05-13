H1,M1,H2,M2,K = map(int,input().split())

duration_min = (H2-H1) * 60 + (M2 - M1)
start_duration_min = duration_min - K

if start_duration_min > 0:
	print(start_duration_min)
else:
	print(0)

