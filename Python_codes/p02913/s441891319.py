# -*- coding: utf-8 -*-
import sys
N=int(sys.stdin.readline().strip())
S=sys.stdin.readline().strip()

def isok(d):    #長さdの文字列で重ならない2つの文字列が存在するかを判定
    D={}    #出てきた文字列:スタート位置
    for i in range(N-d+1):
        x=S[i:i+d]
        if x not in D:  #前に文字列が出てきていない場合
            D[x]=i
        else:  #既に文字列が出てきている場合
            if d<=i-D[x]:   #文字列が重なっていない場合
                return True
            else:           #文字列が重なっていた場合
                pass        #更に右側の文字列を探すために処理を継続する
    else:
        return False

h=N
l=0
while h-l!=1:
    m=(h+l)/2
    if isok(m):
        l=m
    else:
        h=m
print l
