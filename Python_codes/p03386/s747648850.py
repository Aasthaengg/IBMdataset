A, B, K = map(int, input().split())
if B-A+1 >= 2*K: # A以上B以下の整数の数が2K以上
    res_list = [i for i in range(A, A+K)] + [i for i in range(B-K+1, B+1)]
else: # A以上B以下の整数の数が2K未満
    res_list = [i for i in range(A, B+1)]
for i in res_list:
    print(i)