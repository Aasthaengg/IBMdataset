import numpy as np
n,m,k = map(int,input().split())
a = np.array([int(i) for i in input().split()], dtype='int64')
b = np.array([int(i) for i in input().split()], dtype='int64')

# 読まないという選択肢を先頭に入れておく
a_c = np.zeros(n+1,dtype='int64')
a_c[1:] = np.cumsum(a)

b_c = np.zeros(m+1,dtype='int64')
b_c[1:] = np.cumsum(b)

a_c = a_c[a_c <= k]
b_c = b_c[b_c <= k]

ans_l = np.searchsorted(b_c, k - a_c, side='right') - 1
ans_l += np.arange(len(a_c))
print(ans_l.max())