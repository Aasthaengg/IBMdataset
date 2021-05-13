n = int(input())
au = list(map(int,input().split()))
ad = list(map(int,input().split()))
maxi = 0
for i in range(n):
    maxi = max(maxi,sum(au[:i+1])+sum(ad[i:]))
print(maxi)