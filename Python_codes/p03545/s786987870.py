def main():
	S = list(str(input()))
	LenP = 3
	ans = 0
	for i in range(2**LenP):
		P = ["-"]*LenP
		for j in range(LenP):
			if i >> j & 1:
				P[j] = "+"
		Res = [None] * (len(S)+len(P))
		Res[1::2],Res[::2] = P,S
		ResEval = "".join(Res)
		if eval(ResEval) == 7:
			ans = ResEval+"=7"
			print(ans)
			break

if __name__ == '__main__':
	main()