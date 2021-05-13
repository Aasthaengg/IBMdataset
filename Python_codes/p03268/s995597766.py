N,K = map(int,input().split())

#Kが奇数の場合、N mod K = 0を満たす数の3乗が解
if K % 2 == 1:
    print((N // K) ** 3)

#Kが偶数の場合、Kで割って0あまるものの個数とK / 2あまるものの個数の3乗が解
else:
    K2 = K // 2
    #Kで割ってK / 2余る個数を算出
    half = (N // K2 - N // K)
    print(half ** 3 + (N // K) ** 3)
