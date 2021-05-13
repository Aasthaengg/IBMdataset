N, M = map(int, input().split())
Alst = list(map(int, input().split()))

Alst.sort(reverse = True)
k = sum(Alst) / M
if Alst[M-1] < k/4:
    print('No')
else:
    print('Yes')