I=input
A,B,C,X,s=int(I()),int(I()),int(I()),int(I()),0
for i in range(A+1):
    for j in range(B+1):
        for k in range(C+1):
            if 500*i+100*j+50*k==X:s+=1
print(s)