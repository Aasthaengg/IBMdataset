#ネットのやつ　自分で考える
#from math import ceil
#n, h = map(int, input().split( ))
N = int(input())
D = list(map(int, input().split( )))
D1 = sorted(D)
n = N//2
print(D1[n] - D1[n-1])