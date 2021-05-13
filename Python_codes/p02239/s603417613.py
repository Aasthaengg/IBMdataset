# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 10:56:33 2018

@author: maezawa
"""
n = int(input())
adj = [[] for _ in range(n)]
d = [-1 for _ in range(n)]
d[0] = 0


for j in range(n):
    ain = list(map(int, input().split()))
    u = ain[0]
    k = ain[1]
    for i in range(k):
        adj[u-1].append(ain[i+2]-1)
    adj[u-1].sort()
    #print(*adj[u-1])

stack = [0]

while stack:
    #print(stack)
    current = stack[-1]
    flag = 0
    for k in adj[current]:
        if d[k] < 0:
            d[k] = d[current]+1
            stack.append(k)
            flag = 1
        elif d[k] > d[current]+1:
            d[k] = d[current]+1
            stack.append(k)
            flag = 1
    if flag == 0:
        stack.pop()

    #print('current = {}, t = {}'.format(current, t))
    #print('stack', *stack)

for i in range(n):
    print('{} {}'.format(i+1, d[i]))

