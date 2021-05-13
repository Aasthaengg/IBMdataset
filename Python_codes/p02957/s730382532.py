A,B = map(int,input().split())
print("IMPOSSIBLE" if (A+B)%2!=0 else int((A+B)/2))
