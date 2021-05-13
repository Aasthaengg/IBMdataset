n = int(input())

x = 'No'
if 1 <= n <= 81:
    for s in range(1,10):
        for t in range(1,10):
            if n == s*t:
                x = 'Yes'
print(x)