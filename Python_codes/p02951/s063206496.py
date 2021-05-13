#! python3
#  solve_136A.py

A,B,C = map(int,input().split())

print(C-min(A-B,C))