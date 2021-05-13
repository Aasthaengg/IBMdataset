N = [int(e) for e in input().split()]
if(N[0]*2>=N[1]):
    ans = N[1]//2
    print(ans)
else:
    ans = N[0] + (N[1] - N[0]*2)//4
    print(ans)