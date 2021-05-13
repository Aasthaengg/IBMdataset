N,A,B,C,D =list(map(int,input().split()))
s = input()
flag = 0
if C<D:
    if s[B-1:D].count('##') == 0 and s[A-1:C].count('##') == 0:
        print('Yes')
    else:
        print('No')
else:
    if (s[B-2:D+1].count('...')>=1) and (s[A-1:C].count('##') == 0 ):
        print('Yes')
    else:
        print('No')