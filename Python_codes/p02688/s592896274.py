nk = input().split()
n = int(nk[0])
k = nk[1]
l = []

for i in range(int(k)):
    num = int(input())
    sweet = input().split()
    for j in range(num):
        sw = int(sweet[j])
        l.append(sw)

l = list(set(l))

ass = len(l)

ans = n - ass

print(ans)