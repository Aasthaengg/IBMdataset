n, k = map(int,input().split())
w = [int(input()) for _ in range(n)]

# 荷物の最大積算量を返す
def check(p):
    global n,k,w
    v = 0
    track = 0
    temp = 0
    i = 0
    while track < k:
        temp = 0
        while temp + w[i] <= p:
            temp += w[i]
            i = i + 1
            if i == n:
                return i
        track += 1
        #print(track,i)
    return i

def main():
    global n,k,w
    left = 0
    right = 100000*10000

    while True:
        mid = int( (left+right) / 2 )
        #print(left,right,mid)
        v = check(mid)
        judge = check(mid-1)
        #print(n,v,judge)
        if v < n:
            left = mid + 1
        elif v == n and judge != n:
            return mid
        elif v == n and judge == n:
            right = mid

print(main())

