a,b = map(int,input().split())
print("Possible" if a%3 == 0 else "Possible" if b%3 == 0 else "Possible" if (a+b)%3 == 0 else "Impossible")