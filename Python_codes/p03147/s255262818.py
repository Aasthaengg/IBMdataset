n = int(input())
h = list(map(int, input().split()))
res = 0

while max(h) > 0:
    i = 0
    while i < n:
        if h[i] == 0:
            i += 1
        else:
            res += 1
            while i < n and h[i] > 0:
                h[i] -= 1
                i += 1
    
print(res)