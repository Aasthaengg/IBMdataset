#!/usr/bin/env python3
import sys

n,a,b = map(int,input().split())
#print(min(abs(n-a),abs(n-b)))
print("A" if abs(n-a) < abs(n-b) else "B" )