import bisect

N = input()
N = int(N)
L = list(map(int,input().split()))

L_sorted = sorted(L, reverse = False)#昇順

count = 0
for i in range(N):#aの選び方
    for j in range(i+1,N):#bの選び方
        a = L_sorted[i]
        b = L_sorted[j]#b <= c < a+b
        count += bisect.bisect_left(L_sorted, a+b) - j -1
print(count)