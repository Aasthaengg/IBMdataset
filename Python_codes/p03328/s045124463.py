a,b = map(int,input().split())
delta = b-a
tower_b = (delta+1)*delta//2
print(tower_b - b)