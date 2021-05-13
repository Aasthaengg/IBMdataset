a,b = map(int, input().split())
dif = b-a
tower_r = ((1+dif)*dif)//2
print(tower_r-b)