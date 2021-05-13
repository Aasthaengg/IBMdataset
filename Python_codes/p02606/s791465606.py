#!/usr/bin/env python3

import sys
input=sys.stdin.readline

l,r,d=map(int,input().split())
cnt1=r//d
cnt2=(l-1)//d
print(cnt1-cnt2)
