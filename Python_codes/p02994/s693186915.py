n,l = map(int,input().split())
ans = 0
pie = l*n+(1+n)*n//2-n
max_a = l+n-1
min_a = l
if max_a<0:
    ans = pie-max_a
elif min_a<=0 and max_a>=0:
    ans = pie
elif min_a>0:
    ans = pie-min_a
print(ans)