a, b = map(int, input().split())
print(1000000 if a==b==1 else max((4-a)*100000, 0)+max((4-b)*100000, 0))