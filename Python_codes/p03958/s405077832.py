k,t = map(int,input().split())
ls = list(map(int,input().split()))
mx = max(ls)
print(max(0,2*mx-1-sum(ls)))