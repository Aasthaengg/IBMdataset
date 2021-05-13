N = input()
A = map(int, raw_input().split())
ans = 0
flag = True
while flag:
    flag = False
    for j in xrange(N-1, 0, -1):
        if A[j] < A[j-1]:
            ans += 1
            A[j], A[j-1] = A[j-1], A[j]
            flag = True
print ' '.join(map(str, A))
print ans