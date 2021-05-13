N,K=map(int,input().split()) #int複数入力
alist = list(map(int, input().split()))
count = 0
for i in range(0,N):
    if alist[i] >= K:
        count += 1
print(count)