n,a,b,c,d = list(map(int, input().split()))
a,b,c,d = a-1,b-1,c-1,d-1 #indexに合わせる
s = input()
k = 0
swappable = False
possible = True

#A-C, B-D に岩が二つ並んでいる箇所があるなら不可能

#C>Dの場合B以上の位置で3マス以上の空白があれば
for i in range(a, max(c,d)):#+1):
    j = s[i]
    if j=='#':
        if (k==0) and ((a<i<c) or (b<i<d)):
            possible = False
            break
        k = 0
    if j=='.':
        k += 1
        if (k>=3) and (b<i<=(d+1)):
            swappable = True
    

if (c>d) and (not swappable):
    possible = False

print('Yes' if possible else 'No')