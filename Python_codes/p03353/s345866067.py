s = input()
N = len(s)
K = int(input())
ss = []
for i in range(N):
    for j in range(1,6):
        if  i+j <= N:
            ss.append(s[i:i+j])

a = list(set(ss))
a.sort()
print(a[K-1])