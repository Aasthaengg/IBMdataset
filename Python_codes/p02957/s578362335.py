A,B = [ int(i) for i in input().split() ]

print(int((A+B)//2) if (A+B)%2 == 0 else "IMPOSSIBLE")
