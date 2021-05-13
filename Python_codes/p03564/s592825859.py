n = int(input())
k = int(input())

i = 0
ans = 1
while True:
    if i == n:
        print (ans)
        exit ()
    else:
        i += 1
        if ans*2 < ans+k:
            ans *= 2
        else:
            ans += k
