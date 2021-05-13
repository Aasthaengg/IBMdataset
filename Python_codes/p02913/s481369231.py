def z_algorithm(s: str) -> list:
	n = len(s)
	Z = [0] * n
	Z[0] = n
	i, j = 1, 0
	while i < n:
		while i + j < n and s[j] == s[i + j]:
			j += 1
		Z[i] = j
		if j == 0:
			i += 1
			continue
		k = 1
		while i + k < n and k + Z[k] < j:
			Z[i + k] = Z[k]
			k += 1
		i += k
		j -= k
	return Z


def main():
	n = int(input())
	s = input()
	ans = 0
	for i in range(n):
		t = max(min(i,x) for i,x in enumerate(z_algorithm(s[i:])))
		ans = max(ans, t)
	print(ans)

if __name__ == '__main__':
	main()