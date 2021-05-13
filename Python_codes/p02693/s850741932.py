K=int(input())
A,B=map(int,input().split())
C=int(B/K)
i=0
for a in range(C+1):
    i=i+K
    if i>=A and i<=B:
        print("OK")
        break
    if i>B:
        print("NG")
        
