n,c,k = map(int,input().split())
t = [0]*n
for i in range(n):
    t[i] = int(input())
t.sort()
ind = 0
ans = 0
bus = 0
while ind <= n-1:
    bus += 1
    ind_o = ind
    for i in range(c):
        if ind_o+i > n-1:
            ind_o += i-1
            break
        if t[ind_o+i] > t[ind_o]+k:
            break
        else:
            ind += 1
print(bus)