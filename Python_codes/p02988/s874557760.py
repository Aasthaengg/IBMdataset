# Ordinary Number
n = int(input())
p = list(map(int, input().split()))
ct= 0
C = []
for i in range(1,n-1):
    C.append(p[i])
    C.append(p[i-1])
    C.append(p[i+1])
    C.sort()
    if C[1] == p[i]:
        ct +=1
        C = []
    else:
        C = []
print(ct)
