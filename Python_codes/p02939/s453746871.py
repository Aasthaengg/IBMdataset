S = input()
N = len(S)
a = [0]*(N+1)
b = ['']*(N+1)
s = ''
for i in range(1, N+1):
    s += S[i-1]
    b[i] = s
    if s != b[i-1]:
        a[i] = a[i-1]+1
        s = ''
    else:
        a[i] = a[i-1]
print(a[N])
