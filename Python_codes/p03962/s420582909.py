abc=sorted(list(map(int,input().split())))
if abc[0]==abc[2]:
    print(1)
elif abc[0]==abc[1] or abc[1]==abc[2]:
    print(2)
else:
    print(3)
