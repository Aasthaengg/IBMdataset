##かっこいい実装
import numpy as np
#mod = 10**9+7
#n = int(input())
#a = np.fromstring(input(), dtype = np.int64, sep = ' ')
#
#result = 0
#for i in range(60):
#    count_one = int((a&1).sum())
#    result += count_one*(n-count_one)*(2**i)
#    a >>= 1
#print(result%mod)

N = int(input())
A = np.fromstring(input(),dtype = np.int64, sep = ' ')
Large = 10**9 + 7
ans = 0
for i in range(60):
    sum1 = int((A&1).sum())
    ans += sum1*(N-sum1) * 2**i
    #ans %= Large
    A>>=1 # A = A>>1とする
print(ans%Large)






