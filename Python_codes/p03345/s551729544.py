A,B,C,K=map(int,input().split())
if K%2==0:
    val=A-B
    if abs(val)>pow(10,18):
        print("Unfair")
    else:
        print(val)
else:
    val=B-A
    if abs(val)>pow(10,18):
        print("Unfair")
    else:
        print(val)