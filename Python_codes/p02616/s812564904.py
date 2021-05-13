# coding: utf-8
# Your code here!

# リストxsの総乗
def inf_product(xs):
    limit = int(1e9) + 7
    p = 1
    for x in xs:
        p *= x
        p %= limit
    return p

def calp():
    '''
    import random
    limit = int(1e9)
    n = int(2e5)
    k = int(n*9/10)
    x = []
    for i in range(n):
        x.append(random.randint(-limit,limit))
    '''
    n,k = map(int,input().split())
    x = list(map(int,input().split()))
    
    # n=kであれば、全要素の総乗をpとして返す
    if n == k:
        return inf_product(x)
    # 要素0の個数がn-kより大きければ、pとして0を返す
    if x.count(0) > n-k:
        return 0

    #要素を負の配列x1 と 正の配列x2 0の配列x3に分ける
    x.append(0)
    x.sort()
    #print(x)
    m1 = x.index(0)
    m2 = x.count(0)
    x1 =x[:m1]
    x2 =x[m1+m2:]
    x3 =x[m1:m1+m2-1]
    #print(x1,x2,x3)

    # 正の要素がない場合、kが偶数の場合小さい順（絶対値の大きい順）に拾う
    # kが奇数で要素に0を含む場合は、0を返す
    # kが奇数で要素に0を含まない場合は、大きい順（絶対値の小さい順）に拾う
    if len(x2) == 0:
        if k%2 == 0:
            return inf_product(x1[:k])
        elif len(x3) != 0:
            return 0
        else:
            return inf_product(x1[-k:])

    # kが奇数の場合、正のリストの最大のものをまず1個選択する
    p = 1
    if k%2 ==1:
        p *= x2[-1]
        x2.pop(-1)
        k -= 1

    x1b,x2b = [],[]
    for i in range(0,2*int(len(x1)/2),2):
        x1b.append(x1[i]*x1[i+1])
    x2.sort(reverse=True)
    for i in range(0,2*int(len(x2)/2),2):
        x2b.append(x2[i]*x2[i+1])
    
    x1b.extend(x2b)
    x1b.sort(reverse=True)
    x1b.insert(0,p)
    #print(x1b,int(k/2)+1)
    temp = int(k/2)

    if len(x1b) > temp:
        return inf_product(x1b[:int(k/2)+1])
    else:
        if len(x3) != 0:
            return 0
        else:
            return(-1)

print(calp())
