n = int(input())
h = list(map(int,input().split()))

if len(h) == 1 :
    print("Yes")
else :
    h.reverse()
    for i in range(n-1):
        if h[i] < h[i+1] :
            h[i+1] -= 1
            if h[i] < h[i+1] :
                print("No")
                break
    else :
        print("Yes")
