K,N=[int(s) for s in input().split()]
ls=[int(s) for s in input().split()]
ls_sub=[ls[i]-ls[i-1] for i in range(N)]
ls_sub[0]+=K
print(K-max(ls_sub))