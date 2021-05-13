N = int(input())
A = [int(input()) for _ in range(N)]

odd_flag = False
for a in A:
    if a % 2 == 1:
        odd_flag = True
        break

if odd_flag:
    print("first")
else:
    print("second")
