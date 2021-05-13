n,m = map(int, input().split())
d = [list(map(int, input().split()))[1:] for _ in range(m)]
s = list(map(int, input().split()))

count = 0

for i in range(2**n):

    for j in range(m):
        switch = 0
        for k in range(n):
            if (i >> k) & 1 and k+1 in d[j]:
                switch += 1
        if switch%2 != s[j]:
            break
    else:
        count += 1

print(count)