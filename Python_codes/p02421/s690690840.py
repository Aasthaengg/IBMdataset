# coding:utf-8
N=int(input())

taro_pt=0
hanako_pt=0
for i in range(0,N):
    taro_str,hanako_str=map(str,input().split())
    if taro_str>hanako_str:
        taro_pt=taro_pt+3
    elif taro_str<hanako_str:
        hanako_pt=hanako_pt+3
    else:
        taro_pt=taro_pt+1
        hanako_pt=hanako_pt+1

print(str(taro_pt)+" "+str(hanako_pt))