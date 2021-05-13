n = int(input())
a1 = list(map(int,input().split()))
a2 = list(map(int,input().split()))

b1 = [0]
b2 = [0]

for i in range(n):
    b1.append(b1[-1] + a1[i])
    b2.append(b2[-1] + a2[i])

ans = 0

for i in range(n):
    tmp = b1[i+1] + b2[-1] - b2[i]
    ans = max(ans, tmp)

print(ans)
