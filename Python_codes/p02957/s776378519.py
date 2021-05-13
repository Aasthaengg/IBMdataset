n=input().split()
A=int(n[0])
B=int(n[1])
K=int((A+B)/2)
if abs(A-K)==abs(B-K):
    print(K)
else:
    print("IMPOSSIBLE")