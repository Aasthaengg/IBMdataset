S=int(input())
if S==10**18:
    print(0,0,0,10**9,10**9,0)
else:
    print(0,0,(S//10**9)+1,1,10**9-S%10**9,10**9)