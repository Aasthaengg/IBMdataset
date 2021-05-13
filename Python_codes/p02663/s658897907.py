N = list(map(int,input().split()))
res = ((N[2]-N[0])*60) + (N[3]-N[1]) - N[4]
print(res)