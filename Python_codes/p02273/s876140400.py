"""ICGNYN 17D8103016H 土屋　怜"""
import random
import math

def hura (a):
    ind=1
    for i in range(len(a)-1):
        c= [(a[i*4+1][0]-a[i*4][0])/3+a[i*4][0], (a[i*4+1][1]-a[i*4][1])/3+a[i*4][1]]
        d=[(a[i*4+1][0]-a[i*4][0])*2/3+a[i*4][0], (a[i*4+1][1]-a[i*4][1])*2/3+a[i*4][1]]
        cos=math.cos(math.pi/3)
        sin=math.sin(math.pi/3)
        f = [d[0]-c[0],d[1]-c[1]]
        b= [f[0]*cos-sin*f[1]+c[0],sin*f[0]+cos*f[1]+c[1]]
        a.insert(ind,c)
        a.insert(ind+1,b)
        a.insert(ind+2,d)
        ind=ind+4
        

N = int(input())
x=[[0,0],[100,0]]
for i in range(N):
    hura(x)
for i in range(len(x)):
  print(x[i][0],end="")
  print(" ",end="")
  print(x[i][1])
