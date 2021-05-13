A,B=list(map(int,input().split()))
print("Possible" if (A*B)%3==0 or (A+B)%3==0 else "Impossible")