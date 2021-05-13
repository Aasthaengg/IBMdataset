N = int(input())
p = []
if N > 0:
    for i in range(500):
        if (2**(2*i)-1)/3 < N <= (2**(2*(i+1))-1)/3:
            q = 2*i + 1
if N < 0:
    for i in range(1,500):
        if -(2**(2*i+1)-2)/3 <= N < -(2**(2*i-1)-2)/3:
            q = 2*i
if N == 0:
    q = 1
def cal(n,i):
    if i % 2 != 0:
        if (2**(i-1)-1)/3 < n <= (2**(i+1)-1)/3:
            p.append(1)
            n = n - (-2)**(i-1)
            i = i-1
            if i > 0:
                cal(n,i)
        else:
            p.append(0)
            i = i-1
            if i > 0:
                cal(n,i)
    elif n == 0:
        p.append(0)
        i = i-1
        if i > 0:
            cal(n,i)
    else:
        if -(2**(i+1)-2)/3 <= n < -(2**(i-1)-2)/3:
            p.append(1)
            n = n - (-2)**(i-1)
            i = i-1
            if i > 0:
                cal(n,i)
        else:
            p.append(0)
            i = i-1
            if i > 0:
                cal(n,i)
            
    return p
ans = cal(N,q)
for i in range(len(ans)):
    ans[i] = str(ans[i])
print(''.join(ans))