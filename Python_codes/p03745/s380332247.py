N = int(input())
A = list(map(int,input().split()))

before = A[0]
is_ascending = None
ans = 0
for a in A:
    d = a - before
    if d == 0:
        pass
    else:
        if is_ascending == None:
            is_ascending = d > 0
        elif (is_ascending and d < 0) or (not is_ascending and d > 0):
            ans += 1
            is_ascending = None
    
    before = a

print(ans+1)