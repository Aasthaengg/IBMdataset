n = int(input())
L1,L2 = [],[]
for i in range(n):
    a = input().split()
    L1.append(a[0])
    L2.append(int(a[1]))

s = input()
idx = L1.index(s)
print(sum(L2[idx+1:]))