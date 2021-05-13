#!/usr/bin/env python3
a,b,c=map(int,input().split())
t=a-b-c
print(-t*(t<0)or 0)
