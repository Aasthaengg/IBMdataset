N, M = input().split()
if N=='H':
    N=0
else:
    N=1
if M=='H':
    M=0
else:
    M=1

if N^M==0:
    ans = 'H'
else:
    ans = 'D'
print(ans)