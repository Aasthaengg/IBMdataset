time, rem = list(map(int, input().split()))
if time + rem > 23:
	time = time - 24
print(time + rem)