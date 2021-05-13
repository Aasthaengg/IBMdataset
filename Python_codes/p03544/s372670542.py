N = int(input())

l0 = 2
l1 = 1

if (N == 1):
    ans = 1
else:
    before = l0
    middle = l1
    
    for i in range(N - 1):
        nextt = before + middle
        before = middle
        middle = nextt
    
    ans = nextt

print(ans)
