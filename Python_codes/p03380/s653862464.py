N=int(input())
A=list(map(int,input().split()))

if N > 2:
    A.sort()
    num_total = A[-1]
    A.pop()
    def isOK(index, key, l):
        if l[index] >= key:
            return True
        else:
            return False
    
    def meguru_search(l,key): # key以上の値を持つ最小のインデックスを返す
        left = -1
        right = len(l)

        while (right - left) > 1: # 二分探索
            mid = left + (right - left)//2
            if isOK(mid,key,l):
                right = mid
            else:
                left = mid
        
        return right
    
    if num_total%2 == 0:
        Max = num_total//2 
    else:
        Max = num_total//2 + 1
    
    Maxind1 = meguru_search(A,Max) # Max以上の値を持つインデックス
    Maxind2 = Maxind1 - 1 # Max未満の最大の値を持つインデックス
    abs_1 = abs(Max - A[Maxind1])
    abs_2 = abs(Max - A[Maxind2])
    if abs_1 > abs_2: # Maxに近いほどnCrが大きい
        r = A[Maxind2]
    else:
        r = A[Maxind1]
    print(num_total,r)

else:
    print(max(A),min(A))