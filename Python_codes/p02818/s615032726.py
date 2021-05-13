a,b,k=map(int,input().split())

if a-k>=0 : print("{} {}".format(a-k,b))
else : print("0 {}".format(max(0,b-(k-a))))