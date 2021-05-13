# 135 B

def swap(k, a, b):
    k[a], k[b] = k[b], k[a]
    return k

n = int(input())
l = list(map(int, input().split()))
num = 0
k = []
ans = []

for i in range(len(l)):
    k.append(l[i])

k.sort()

for i in range(n):
    if k[i] != l[i]:
        num += 1
        ans.append(i)

if num == 2 :
    swap(l, ans[0], ans[1])
    if k == l:
        print("YES")
    else:
        print("NO")
elif num == 0:
    print("YES")
else:
    print("NO")
