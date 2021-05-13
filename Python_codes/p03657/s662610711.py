A,B=map(int,input().split())
print("Impossible" if (A+B)%3!=0 and A%3!=0 and B%3!=0 else "Possible")