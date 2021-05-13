n = int(input())
alst = list(map(int, input().split()))
odd_cnt = 0
for a in alst:
    if a % 2 == 1:
        odd_cnt = (odd_cnt + 1) % 2
if odd_cnt == 1:
    print("NO")
else:
    print("YES")