N=int(input())
X=list(map(int,input().split()))

X_dict={}
X_=X.copy()
X_.sort()
for x_idx,x in enumerate(X_):
    X_dict[x]=x_idx

median_idx = N//2-1
for x in X:
#     print('=====')
#     print(x)
    x_sort_idx=X_dict[x]
    if median_idx < x_sort_idx:
        ans = X_[median_idx]
    else:
        ans = X_[median_idx+1]
    print(ans)