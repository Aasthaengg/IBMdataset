from sys import stdin
input = stdin.readline
N = map(int, input().split())
L = list(map(int, input().split()))

c=0

for i in range(len(L)-2):
    for j in range(i+1,len(L)):
        for k in range(j+1,len(L)):
            if L[i]+L[j]>L[k] and L[j]+L[k]>L[i] and L[k]+L[i]>L[j] and L[i]!=L[j] and L[j]!=L[k] and L[k]!=L[i]:c=c+1

print(c)              