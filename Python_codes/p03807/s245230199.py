N = int(input())
A_list = list(map(int,input().split()))
odd_cnt = 0
for i in A_list:
    if i % 2 == 1:
        odd_cnt += 1
if odd_cnt % 2 == 1:
    print("NO")
else:
    print("YES")
