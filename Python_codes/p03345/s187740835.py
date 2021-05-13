A,B,C,K = map(int,input().split())
a = (A-B)*(-1)**(K%2)
print(a if abs(a)<10**18 else "Unfair")