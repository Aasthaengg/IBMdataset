X,N = map(int, input().split())
l = [int(x) for x in input().split()]
i = 1
if X not in l:
        print(X)
else:    
    while i <= N//2 + 1 :
        if X - i  not in l:
            print(X-i)
            break
        elif X + i not in l:
            print(X+i)
            break
        i += 1