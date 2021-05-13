#coding:utf-8
#1_6_D 2015.4.5
n,m = map(int,input().split())
matrix = [list(map(int,input().split())) for i in range(n)]
vector = [int(input()) for i in range(m)]
for j in range(n):
    sum = 0
    for i in range(m):
        sum += matrix[j][i] * vector[i]
    print(sum)