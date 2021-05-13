# coding: utf-8
# Here your code !

num_j = [[[0 for _ in range(10)] for _ in range(3)] for _ in range(4)]

n = int(input())

for _ in range(n):
    b,r,f,v = map(int,input().split())
    num_j[b-1][r-1][f-1] += v

for i in range(4):
    for j in range(3):
        print(" ",end="")       
        print(" ".join(map(str,num_j[i][j])))
    
    if i != 3:
        print("#"*20)