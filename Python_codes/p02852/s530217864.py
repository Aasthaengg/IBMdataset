N, M = [int(item) for item in input().split()]
S = input()
a=[]
s = S
n = N
while n > 0:
    for i in range(M, 0, -1):
        can = False
        if n>=i and s[n-i] == '0':
            a.append(i)
            s = s[:n-i+1]
            n -= i
            can = True
            break
    if (not can) and len(s)>1:
        print(-1)
        a=[]
        break
a=a[-1::-1]
if len(a):
    print(*a)