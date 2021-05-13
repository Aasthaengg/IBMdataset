h,w= map(int,input().split())
n= int(input())
a= list(map(int,input().split()))
st = []
for i in range(1,n+1):
    for c in range(a[i-1]):st.append(i)
ans = [[0 for _ in range(w)] for _ in range(h)]
for i in range(h):
    for j in range(w):ans[i][j]= st[i*w+j]
    if i%2==1:ans[i] = ans[i][::-1]
    print(*ans[i])