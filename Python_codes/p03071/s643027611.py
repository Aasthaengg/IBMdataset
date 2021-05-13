A,B=map(int,input().split())
res = sorted([A,A-1,B,B-1],reverse=True)
print(res[0]+res[1])