import sys
n = int(input())
A=[int(e)for e in sys.stdin]
cnt = 0
G = [797161,265720,88573,29524,9841,3280,1093,364,121,40,13,4,1]
G = [v for v in G if v <= n]
def insertionSort(A, n, g):
    global cnt
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j = j - g
            cnt += 1
        A[j+g] = v
for g in G:
    insertionSort(A, n, g)
print(len(G))
print(*G)
print(cnt)
print(*A,sep='\n')
