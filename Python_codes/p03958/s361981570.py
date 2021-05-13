k, t = map(int,input().split())
A = list(map(int,input().split()))
max_A = max(A)

if t == 1:
    print(k-1)
else:
    if max_A -1 > sum(A) - max_A:
        print((max_A -1) - sum(A) + max_A)
    else:
        print(0)
    
        
