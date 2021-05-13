N,M,D = map(int, input().split())

# 1~Nまでの数字でペアを作るとき、差がDになる組の個数
# (d+1, 1), ..., (N, N - D)のN-D個とこれの左右を入れ替えたやつで2*(N - D)個
tmp = N if D == 0 else (N -D) * 2
# 分母は左右の選び方がそれぞれN個あるのでN**2
# それがM-1項ある
ans = tmp / N**2 * (M-1)

print(ans)