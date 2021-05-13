def check(P):
    lis = [[] for i in range(k)]
    su = [0 for i in range(k)]
    
    su.append(-10000)
    cur = 0
    for i, bag in enumerate(baggage):
        #cur = 0
        #print(su,cur,su[cur])
        while su[cur] + bag > P:
            cur += 1
        if cur == k:
            return False
        else:
            lis[cur].append(bag)
            su[cur] += bag
    #print(lis, su, P)
    return True

def main():
    min_P = 1000000000
    left = 1
    right = 1000000000
    mid = (left + right)//2
    while  left < right:
        '''if (left + right) % 2 == 0:
            mid = (left + right)//2
        else:
            mid = (left + right)//2 + 1
        #print(left, mid, right, end=" ")'''
        
        if check(mid):
            right = mid
            if min_P > mid:
                min_P = mid
        else:
            left = mid + 1
        mid = (left + right)//2
    #print(left,right)
    print(min_P)
if __name__ == '__main__':
    n, k = map(int, input().rstrip().split(" "))
    #n,k= 5,3
    baggage = [int(input()) for i in range(n)]
    #baggage = [8,1,7,3,9]
    
    main()



