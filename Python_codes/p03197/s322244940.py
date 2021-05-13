N = int(input())
flg = False
for i in range(N):
    A = int(input())
    if A % 2:
        flg = True
if flg:
    print("first")
else:
    print("second")