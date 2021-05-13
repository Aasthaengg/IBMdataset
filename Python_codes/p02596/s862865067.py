K = int(input())

powlis = [7*pow(10, i, K) for i in range(K)]
for i in range(K-1):
    powlis[i+1] = (powlis[i] + powlis[i+1]) % K
powlis[0] %= K


try:
    print(powlis.index(0) + 1)
except:
    print(-1)