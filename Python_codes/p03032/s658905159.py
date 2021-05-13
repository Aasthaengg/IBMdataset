def max2(x,y):
    return x if x > y else y
def min2(x,y):
    return x if x < y else y

N, K = map(int, input().split())
V = list(map(int, input().split()))
res = 0
for l in range(K+1):
    for r in range(K+1-l):
        if l+r>N:
            continue
        temp=V[:l]+V[N-r:]
        temp.sort()
        S = sum(temp)
        for cnt in range(min2(K-l-r,l+r)):
            if temp[cnt]<0:
                S -= temp[cnt]
            else:
                break
        res = max2(res, S)
print(res)