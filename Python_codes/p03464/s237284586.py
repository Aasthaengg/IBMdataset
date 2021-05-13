K,*A=map(int, open(0).read().split())
m=2
M=2
for a in A[::-1]:
    if (m+a-1)//a*a>M//a*a:
        print(-1)
        break
    m=(m+a-1)//a*a
    M=M//a*a+a-1
else:
    print(m,M)