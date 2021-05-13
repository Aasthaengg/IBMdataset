import math

N, A, B = map(int, input().split())

sa = B - A + 1;

if sa % 2 == 1 :
	ans = min(N - A, B - 1);
	#chmin(ans, (B - A) / 2);
	ans = min(ans, (B - A) // 2)

	print(ans)
else :
	ans = 10**30;

	# A を 1 に移動させて1勝
	ca = A
	cb = B

	ca = 1;
	cb -= A;

	cand = (cb - ca) // 2 + A;
	ans = min(ans, cand);

	# B を N に移動させて1敗
	ca = A
	cb = B
	cb = N;
	ca += N - B + 1;
	cand = (cb - ca) // 2 + (N - B + 1);

	ans = min(ans, cand);


	print(ans)
