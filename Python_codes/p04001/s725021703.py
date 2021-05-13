def main():
	S = list(str(input()))
	LenP = len(S)-1
	ans = 0
	for i in range(2**LenP):
		P = [""]*LenP
		for j in range(LenP):
			if i >> j & 1:
				P[j] = "+"
		Res = [None] * (len(S)+len(P))
		Res[1::2],Res[::2] = P,S
		ResEval = "".join(Res)
		ans += eval(ResEval)
	print(ans)

if __name__ == '__main__':
	main()