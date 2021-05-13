N = int(input())
*A, = map(int, input().split())

cnt_neg = sum(a < 0 for a in A)
cnt_zero = A.count(0)

if cnt_zero or cnt_neg % 2 == 0:
    print(sum(abs(a) for a in A))
else:
    print(sum(abs(a) for a in A)-2*min(abs(a) for a in A))
