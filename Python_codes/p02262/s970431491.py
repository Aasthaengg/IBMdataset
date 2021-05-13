n = int(raw_input())
a = []
for i in range(n):
    a.append(int(raw_input()))

cnt = 0
num = 1
G = [1]
while 1:
    if num*3+1 > n:
        break
    G.insert(0, num*3+1)
    num = num*3 + 1
m = len(G)

def insertionSort(A, n, g, cnt):
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j = j - g
            cnt += 1
        A[j+g] = v
    return cnt

for i in range(m):
    cnt = insertionSort(a, n, G[i], cnt)

print m
for i in range(m):
    if i == m-1:
        print G[i]
    else:
        print G[i],
        
print cnt

for i in range(n):
    print a[i]