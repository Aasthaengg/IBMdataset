#B - Similar Arrays
N = int(input())
A = list(map(int,input().split()))

all_odd = 1
for i in A:
    if i%2 == 0:
        all_odd *= 2
    else:
        all_odd *= 1
tot_cnt = 3**N

ans = tot_cnt - all_odd
print(ans)