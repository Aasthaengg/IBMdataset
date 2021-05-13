n = int(input())
a = list(map(int, input().split()))

adj = 0
path = []

# aに正も負もあるとき
if any([ai > 0 for ai in a]) and any([ai < 0 for ai in a]):
    
    # |max| >= |min| ならmaxをすべてのaの要素に足せば、aはすべて0以上
    if abs(max(a)) >= abs(min(a)):
        max_a = max(a)
        max_idx = a.index(max_a) + 1
        
        for i, ai in enumerate(a):
            if i+1 == max_idx:
                pass
            else:
                a[i] += max_a    
                path.append((max_idx, i+1))
                
        adj = n-1
    
    # |max| < |min| ならminをすべてのaの要素に足せば、aはすべて0以下    
    else:
        min_a = min(a)
        min_idx = a.index(min_a) + 1
        
        for i, ai in enumerate(a):
            if i+1 == min_idx:
                pass
            else:
                a[i] += min_a   
                path.append((min_idx, i+1))
            
        adj = n-1
        
        

# aがすべて0以上なら累積和の要領で足すようにする
if all([ai >= 0 for ai in a]):
    print(n-1 + adj)
    for i in range(1,n):
        path.append((i, i+1))
        
    for x,y in path:
        print(x,y)
        
# aがすべて0以下なら、a_nから順に累積和の要領で足していく
elif all([ai <= 0 for ai in a]):
    print(n-1 + adj)
    for i in range(n,1,-1):
        path.append((i, i-1))
        
    for x,y in path:
        print(x,y)