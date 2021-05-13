K = int(input())
A,B = list(map(int,input().split()))
if A <= B - (B % K):
    print("OK")
else:
    print("NG")
