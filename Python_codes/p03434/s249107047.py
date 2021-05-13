n = int(input())
arr = list(map(int, input().split()))
alice = 0
bob = 0
chance = "A"
for _ in range(len(arr)):
	i = max(arr)
	if chance == "A":
		alice += i
		chance = "B"
	else:
		bob += i
		chance = "A"
	indx = arr.index(i)
	del arr[indx]
print(alice - bob)