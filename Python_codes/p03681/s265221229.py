#2問目
import math
MAX = 10 ** 9 + 7
N, M = map(int, input().split())
if(abs(N - M) > 1):
    print(0)
elif(abs(N - M) == 0):
    #犬と猿が同数いる時
    print((((math.factorial(N) % MAX) * (math.factorial(M) % MAX) * 2)) % MAX)
else:
    #犬と猿の差が1の時
    print(((math.factorial(N) % MAX) * (math.factorial(M) % MAX)) % MAX)