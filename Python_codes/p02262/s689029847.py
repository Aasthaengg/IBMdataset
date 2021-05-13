import math
n=int(input())
A=[int(input()) for i in range(n)]

def insertion_sort(ar,num,g):
    count=0
    for i in range(g,num):
        v=ar[i]
        j=i-g
        while j>=0 and ar[j]>v:
            ar[j+g]=ar[j]
            j=j-g
            count+=1
        ar[j+g]=v
    return count

def shell_sort(AR,num):
    count=0
    m = math.floor(math.log(2 * n + 1) / math.log(3))
    print(m)
    G = [0 for i in range(m)]   
    G[0] = 1
    for i in range(1, m):
        G[i] = 3 * G[i - 1] + 1
    G.reverse()
    print(*G)
   
    for i in range(m):
        count+= insertion_sort(A, n, G[i])
    print(count)


shell_sort(A,n)
for i in A:
        print(i)
    