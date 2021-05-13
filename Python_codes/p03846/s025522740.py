N = int(input())
A = list(map(int, input().split()))
judge = 1
while 0 in A:
    A.remove(0)

A_ = list(set(A))
A_.sort()
for i in range(len(A_) - 1):
    if A_[i+1] == A_[i]+2:
        judge = 1
    else:
        judge = 0

if len(set(A)) == len(A)/2 and judge:
    print((2 ** (len(A) // 2)) % (10**9 +7))
else:
    print(0)