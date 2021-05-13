k,s = map(int,input().split())
t = 0

for i in range(k+1):
    for j in range(k+1):
        if k >= s - i - j and 0 <= s - i - j:
            t += 1

print(t)