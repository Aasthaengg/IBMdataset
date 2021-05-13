N, K = map(int,input().split())
v = list(map(int,input().split()))
ans = [0]
for i in range(1,min(K,N)+1):
    for a in range(i+1):
        b = i-a
        if b == 0:
           get = v[:a]
        else:
            get = v[:a]+v[-b:]
        get.sort()
        for j in range(min(K-i,len(get))):
            p = get.pop(0)
            if p >= 0:
                A = p + sum(get)
                break
        else:
            A = sum(get+[0])
        ans.append(A)
print(max(ans))