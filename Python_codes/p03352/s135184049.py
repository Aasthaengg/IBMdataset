x = int(input())
cnt = []
for b in range(1, int(x**0.5)+1):
    for p in range(2, 11):
        if b**p <= x:
            cnt.append(b**p)
            
print(max(cnt))