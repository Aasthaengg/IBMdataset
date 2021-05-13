n = int(input())
S = list(input()) + [None]

ans = 1
i = 0
prev = None

while i < n:
    if S[i]==S[i+1]:
        if prev == None:
            ans *= 6
        elif prev == 0:
            ans *= 3
        else:
            ans *= 2
        prev = 0
        i += 2
    else:
        if prev == None:
            ans *= 3
        elif prev == 0:
            ans *= 1
        elif prev == 1:
            ans *= 2
        prev = 1
        i += 1
        
print(ans%1000000007)
