k, x = list(map(int, input().split()))

if k == 1:
    print(x)
else:
    lower = []
    upper = []
    for i in range(1, k):
        lower.append(x-i)
        upper.append(x+i)
    
    res = lower[::-1] + [x] + upper

    r = [str(x) for x in res]
    print(" ".join(r))
