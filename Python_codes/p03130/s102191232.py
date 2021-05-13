import collections
a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())
arr = [a,b,c,d,e,f]
A = collections.Counter(arr).most_common()

if len(A) == 4:
    if A[0][1] == 2 and A[1][1] == 2 and A[2][1] == 1 and A[3][1] == 1:
        print('YES')
    else:
        print('NO')
else:
    print('NO')