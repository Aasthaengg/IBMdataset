# Tenka1_2017_B_Different_Distribution.py

N = int(input())
I = []*N
for i in range(N):
    a, b = list(map(int, input().split()))
    I.append((a, b))
# print(I)
I.sort()
k = I[0][0]
l = I[-1][0]
m = I[-1][1]
# print(k,l,m)
print((k-1)+(l-k+1)+m)
