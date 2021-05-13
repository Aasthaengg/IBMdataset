# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 15:42:52 2020

@author: tinku
"""
def converter(arr,m,n):
    new_arr=[[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            if arr[i][j]=='.':
                new_arr[i][j]=0
            else:
                new_arr[i][j]=1
    return new_arr
            
m,n=map(int,input().split())
arr=[]
for i in range(m):
    arr.append(input())
arr=converter(arr,m,n)
if arr[0][0]==1 or arr[m-1][n-1]==1:
    print(0)
else:
    arr[0][0]=1
    for i in range(1,m):
        arr[i][0]=int(arr[i-1][0]==1 and arr[i][0]==0)
    for i in range(1,n):
        arr[0][i]=int(arr[0][i-1]==1 and arr[0][i]==0)
    for i in range(1,m):
        for j in range(1,n):
            if arr[i][j]==0:
                arr[i][j]=arr[i-1][j] + arr[i][j-1]
            else:
                arr[i][j]=0
    print((arr[m-1][n-1])%(10**9 +7))