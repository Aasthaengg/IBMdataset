c=[list(map(int,input().split()))for i in range(3)]
a=[c[0][i]-0 for i in range(3)]
b=[c[i][0]-a[0]for i in range(3)]
d=[[a[i]+b[j] for i in range(3)]for j in range(3)]
print('Yes' if c==d else 'No')