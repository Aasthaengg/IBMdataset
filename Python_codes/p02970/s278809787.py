[N,D] = list(map(int,input().split()))

if N%(2*D+1)!=0:
    out = N//(2*D+1) +1
else:
    out = N//(2*D+1)

print(out)