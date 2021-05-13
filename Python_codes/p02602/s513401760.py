n, k = map(int, input().split())
A = list(map(int, input().split()))

for i in range(n - k): #iはスタート地点
    old = A[i] #Aのj番目の要素をかける
    new = A[i + k]
    
    if old < new:
        print("Yes")
    else:
        print("No")