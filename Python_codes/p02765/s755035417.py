n=[int(i) for i in input().split()]
if n[0]<10:
    print(100*(10-n[0])+n[1])
else:
    print(n[1])