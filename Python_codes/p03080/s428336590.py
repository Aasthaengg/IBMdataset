N=int(input())
S=input()
print("YNeos"[S.count("R")<=S.count("B")::2])