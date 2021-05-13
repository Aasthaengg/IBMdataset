n = int(input())
s = input()
t = input()
pointer = 0
ans = [1,0]
mod = 1000000007
while pointer < n:
	if s[pointer] == t[pointer]:

		pointer += 1
		if ans[1] == 0:
			ans[0] = ans[0] *3
		elif ans[1] == 1:
			ans[0] = ans[0] *2
		#ans[0] = ans[0] % mod
		ans[1] = 1

	else:

		pointer += 2
		if ans[1] == 0:
			ans[0] = ans[0] *6
		elif ans[1] == 1:
			ans[0] = ans[0] *2
		elif ans[1] == 2:
			ans[0] = ans[0] *3
		#ans[0] = ans[0] % mod
		ans[1] = 2

print(ans[0] % mod)