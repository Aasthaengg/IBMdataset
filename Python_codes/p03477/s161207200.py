A,B,C,D=map(int,input().split())
e=A+B-C-D
print("Balanced")if e==0 else print(["","Left","Right"][int(e/abs(e))])
