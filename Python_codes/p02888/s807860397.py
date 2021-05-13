N = int(input())
L = list(map(int,input().split()))
L.sort()
cnt = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        h_min = j
        h_max = N
        while h_max - h_min != 1:
            h_mid = (h_max + h_min) // 2
            if L[i] + L[j] > L[h_mid]:
                h_min = h_mid
            else:
                h_max = h_mid
        cnt += h_min - j
print(cnt)