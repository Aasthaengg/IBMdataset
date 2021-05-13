# coding: utf-8
# Your code here!

N = int(input())
d = list(map(int, input().split()))
dc = d[:]

ans = []

for i, v in enumerate(d):    
    for j, w in enumerate(dc):
        # print(i, j)
        if (i == j):
            continue        
        ans.append(v * w)

print(int(sum(ans)/2))