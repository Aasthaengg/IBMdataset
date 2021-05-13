# CODE FESTIVAL 2016 Final
# B - Exactly N points
# https://atcoder.jp/contests/cf16-final/tasks/codefestival_2016_final_b
N = int(input())
for i in range(1, N+1):
    if i*(i+1)//2 >= N:
        k = i
        break


S = k*(k+1)//2
sub = S-N
for i in range(1, k+1):
    if i == sub:
        continue
    print(i)
1
