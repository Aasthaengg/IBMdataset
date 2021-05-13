n = int(input())
H = list(map(lambda x: int(x)-1, input().split()))
for i in range(n-1):
    if H[i] > H[i+1]:
        if H[i] <= H[i+1] + 1:
            # 次に1を足して大きいならOK
            # 足した場合は記録する
            H[i+1] += 1
        else:
            print('No')
            break
else:
    print('Yes')