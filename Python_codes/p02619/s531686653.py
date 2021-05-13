#import random
import numpy as np
d=int(input())
c=np.array(list(map(int,input().split())))
s=[None]*d
r0=[None]*d
r1=[None]*d
cm=np.array([0]*26)
cd=np.array([0]*26)
t=[None]*d
for i in range(d):
  s[i]=list(map(int,input().split()))
s=np.array(s)
for i in range(d):
  t[i]=int(input())-1
"""
for j in range(d):  
  #rand = np.random.randint(26, size = 10) 
  #print(np.argmax(s[j])+1)
  r_i=np.argmax(s[j])
  cd=c*cm
  if np.max(cd>s[i][r_i]):
    r_i=np.argmax(cd)
  r0[j]=r_i
  for k in range(26):
    cm[k]+=1
  cm[r_i]=0
  #r_i+=1
  #print(r_i)
cm=np.array([0]*26)
cd=np.array([0]*26)  
rand = np.random.randint(100, size = d) 
for j in range(d):  
  #print(np.argmax(s[j])+1)
  r_i=r0[j]
  cd=c*cm
  if rand[j]>80:
    r_i=np.argmax(cd)
  r1[j]=r_i
  for k in range(26):
    cm[k]+=1
  cm[r_i]=0
"""
r0=t
score=0
cm=np.array([0]*26)
cd=np.array([0]*26)  
for j in range(d):
  r0_j=r0[j]
  score+=s[j][r0_j]
  for k in range(26):
    cm[k]+=1
    cm[r0_j]=0
  cd=c*cm
  score+=-np.sum(cd)
  print(score)
  
    

