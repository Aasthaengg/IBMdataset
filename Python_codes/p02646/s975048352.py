import math
import collections
import itertools
import copy

def YesNo(Bool):
    if(Bool):
        print("YES")
    else:
        print("NO")
    return

def resolve():

    A,V=map(int,input().split())
    B,W=map(int,input().split())
    T=int(input())

    if(A<B and V<=W):
        print("NO")
        return

    if(A>B and V<=W):
        print("NO")
        return

    if(A<B):
        if(A+V*T >= B+W*T):
            print("YES")
        else:
            print("NO")
    else:
        if(A-V*T <= B-W*T):
            print("YES")
        else:
            print("NO")

resolve()
