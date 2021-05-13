# coding: utf-8
# Your code here!
H,W,A,B=map(int,input().split())

ans=[]
for b in range(B):
    ans.append(["1"]*A+["0"]*(W-A))
for b in range(H-B):
    ans.append(["0"]*A+["1"]*(W-A))

for item in ans:
    print("".join(item))