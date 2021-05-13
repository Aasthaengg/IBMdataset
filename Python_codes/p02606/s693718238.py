L, R, d = input().split()
if int(L)%int(d) == 0:
    print(int(R)//int(d) - int(L)//int(d) + 1)
else:
    print(int(R)//int(d) - int(L)//int(d))

