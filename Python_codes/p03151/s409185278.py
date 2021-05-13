n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
cnt = 0
need = 0
sup = []
for i in range(n):
    k = B[i] - A[i]
    if k > 0:
        need += k
        cnt += 1
    else:
        sup.append(-k)
sup.sort()
while need > 0:
    if sup:
        need -= sup.pop()
        cnt += 1
    else:
        print(-1)
        break
else:
    print(cnt)