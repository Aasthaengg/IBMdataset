N = int(input())
a = list(map(int,input().split()))
a.sort(reverse=True)
st_n = a[0]
st_r = a[1]
m = st_r*(st_n-st_r)
for r in range(2,N):
    cn = a[r]*(st_n-a[r])
    if m < cn:
        st_r = a[r]
        m = cn
print(st_n,st_r)