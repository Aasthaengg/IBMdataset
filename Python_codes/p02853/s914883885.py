a, b = map(int, input().split())
if a==b==1:
    print(1000000)
else:
    print(max((4-a)*100000, 0)+max((4-b)*100000, 0))