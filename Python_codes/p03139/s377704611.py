n,a,b=map(int,input().split())
ans_max=min(a,b)
ans_min=max(a+b-n,0)
print(ans_max,ans_min)