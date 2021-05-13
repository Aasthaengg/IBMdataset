N = int(raw_input())
A = map(int, raw_input().split())
count = 0
flag = True
while flag:
    flag = False
    for i in xrange(N-1, 0, -1):
        if A[i-1] > A[i]:
            A[i-1], A[i] = A[i], A[i-1]
            count+=1
            flag = True
print ' '.join(map(str, A))
print count