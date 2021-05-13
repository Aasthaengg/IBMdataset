n = int(input())
A = list(map(int,input().split()))
s = [0]

for i in A:
    s.append(i+s[-1])

M = 10000000000

for i in range(1,len(s)-1):
    dif = abs((s[-1]-s[i]) - s[i])
    M = min(M,dif)

print(M)