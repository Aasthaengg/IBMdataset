n,m,d = map(int, input().split())
# for each section, mean is:
# (n*2-d*2)/(n^2)
# ex. n=7, d=2
# (1,3) (2,4) (3,5) (3,1) (4,6) (4,2) (5,7) (5,3) (6,4) (7,5)
ans = (n-d)*2/(n*n)*(m-1)
if d==0: ans /= 2
print(ans)