import os,sys
a=input().split(' ')
n=[int(i) for i in a]
m=[n[0]*n[2],n[0]*n[3],n[1]*n[2],n[1]*n[3]]
print(max(m))
