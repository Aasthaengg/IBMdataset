T1, T2 = map(int, input().split())
A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())
mid = (A1 - B1) * T1
end = mid + (A2 - B2) * T2
if end == 0:
	print("infinity")
elif mid*end > 0:
	print(0)
else:
	if mid % end == 0:
		print(-2*(int(mid/end)))
	else:
		print(1-2*(int(mid/end)))