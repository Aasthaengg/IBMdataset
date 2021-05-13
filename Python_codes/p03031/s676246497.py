def main():
	N, M = [int(n) for n in input().split(" ")]
	lights_def = [[0] * (N + 1) for i in range(M)]
	# lights_def[i] = List, i-th light (i = 0 ~ M)
	# lights_def[i][j] = 1 / 0, j-th switch is related (j = 1 ~ N)
	for i in range(M):
		tmp = [int(t) for t in input().split(" ")]
		for j in tmp[1:]:
			lights_def[i][j] = 1
	p = [int(x) for x in input().split(" ")]
	for i in range(len(p)):
		lights_def[i][0] = p[i]

	cnt = 0
	for i in range(2 ** N):
		switch_bit = list(pad_zero(format(i, 'b'), N))
		for j in range(len(lights_def)):
			light = lights_def[j]
			if sum([light[k + 1] for k in range(len(switch_bit)) if switch_bit[k] == "1"]) % 2 != light[0]:
				break
		else:
			cnt += 1

	print(cnt)

def pad_zero(s, n):
	s = str(s)
	return (("0" * n) + s)[-n:]

main()