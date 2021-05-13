N,A,B,C,D=map(int,input().split())
S=input()
if "##" in S[A-1:max(C,D)] or ("..." not in S[B-2:min(C,D)+1] and C>D):
    print("No")
else:
    print("Yes")