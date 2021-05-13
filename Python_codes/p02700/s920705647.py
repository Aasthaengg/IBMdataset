A, B, C, D = map(int, input().split())
t = 1
a = 1
if C%B==0:
    t = 0
if A%D==0:
    a = 0

if C//B+t <= A//D+a:
    print('Yes')
else:
    print('No')
