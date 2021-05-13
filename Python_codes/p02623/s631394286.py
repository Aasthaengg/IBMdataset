import sys
input = sys.stdin.readline

n, m, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))


#Aだけのときのmax

s = 0
j = 0
for i in range(n):
    if s + a[i] > k:
        break
    else:
        s += a[i]
        j += 1


ans = [j]

for l in range(m):
    flag = True
    s += b[l]
    while s > k:
        s -= a[j-1]
        j -= 1
        if j < 0:
            flag = False
            break
    
    if not flag:
        break
    else:
        ans.append(l + 1 + j)
        #print(ans)

print(max(ans))
