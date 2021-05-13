a,b,c = list(map(int,input().split()))
print("A") if abs(b-a) < abs(c-a) else print("B")