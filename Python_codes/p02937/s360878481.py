ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

s = input()
t = input()

A = [[] for i in range(26)]

for i in range(len(s)):
    A[ord(s[i]) - ord("a")].append(i+1)

from bisect import bisect_left as bl
'''index  =  bl(list,num)'''
nagasa = len(s)
ans = 0
ima = 0
mae = 0
for i in range(len(t)):
    tmp = bl(A[ord(t[i]) -ord("a")],ima+1)
    if tmp == len(A[ord(t[i]) -ord("a")]):
        ans += nagasa - ima
        ima = 0
        tmp = bl(A[ord(t[i]) -ord("a")],ima+1)
        if tmp == len(A[ord(t[i]) -ord("a")]):
            print(-1)
            exit()
    mae = ima
    ima = A[ord(t[i]) -ord("a")][tmp]
    ans += ima - mae
print(ans)

