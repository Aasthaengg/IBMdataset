a,b,c=map(int,input().split())
print(min(a*b*(c-(c//2)*2),a*c*(b-(b//2)*2),c*b*(a-(a//2)*2)))

