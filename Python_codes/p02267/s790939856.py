def linearSearch(n, S, q, T):
    count = 0
    if n <= q:
        for i in S:
            if i in T:
                count += 1
        print(count)
                
    else:
        for k in T:
            if k in S:
                count += 1
        print(count)
                
    

n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

linearSearch(n, S, q, T)