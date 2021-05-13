K = int(input())
A, B = input().split()
x = False

for i in range(1, 501):
    if int(A) <= K*i <= int(B):
        x = True

if x:
    print("OK")
else:
    print("NG")