N = int(input())
A_list = [int(e) for e in input().split()]

#全通りは 2**(N-1)なのでTLEする

#操作を考えると、-に対しては移動or打ち消しとなる。
#繰り返していくと-はどんどん打ち消される。
#最終的には
# - が奇数個 : 1個だけ残る。absをsumしたものから、abs最小分を引けばよい
# - が偶数個 : 全てが打ち消される。 ∴absをsumればOK

min_abs_A = 7 + 10**9
cnt_minus_in_A = 0
sum_abs_A = 0

for A in A_list:
    if A < 0:
        cnt_minus_in_A += 1
        
    if abs(A) < min_abs_A:
        min_abs_A = abs(A)
    
    sum_abs_A += abs(A)
    
if cnt_minus_in_A % 2 == 0:
    print(sum_abs_A)
else:
    print(sum_abs_A - 2*min_abs_A)