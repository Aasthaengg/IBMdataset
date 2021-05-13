import math
x=int(input())
def eratosthenes(n):
    """n以下の素数をエラトステネスの篩によって求める.リストをかえす"""
    prime = []
    limit = math.sqrt(n)
    data = [i + 1 for i in range(1, n)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]
ans=eratosthenes(10**5+3)
for i in  range(len(ans)):
    if ans[i]>=x:
        print(ans[i])
        exit()
    else:
        pass