a=int(input())
b=list(map(int,input().split()))
c=[0]*a
"""
for i in range(a):
    c.append(b.index(i+1)+1) #おそらく計算量O(N^2)
"""
for i in range(a):
    c[b[i]-1]=i+1
result = ' '.join(map(str,c))
print(result)