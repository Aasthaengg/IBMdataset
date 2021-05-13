n = int(input())
a = list(map(int,input().split()))
ans = [0]*(n)

ans[n//2]=a[0]

#ケツから１こ飛ばしであたまからいれていく
for i in range(0,n//2,1):
    ans[i]=a[n-1-2*i]
    ans[n-1-i]=a[n-2-2*i]

print(" ".join(map(str,ans)))