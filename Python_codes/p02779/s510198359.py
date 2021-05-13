def has_duplicates(seq):
    return len(seq) != len(set(seq))

N=int(input())
A=list(map(int,input().split()))
if has_duplicates(A):
    print('NO')
else:
    print('YES')