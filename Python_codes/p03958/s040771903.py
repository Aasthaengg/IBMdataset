#!/usr/bin/env python3
k,t = map(int,input().split())	
a = list(map(int,input().split()))
print(max(0,2*(max(a)-(k+1)//2)-1))