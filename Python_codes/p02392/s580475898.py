tmpA = list(map(int,input().split(" ")))
tmpB = sorted(set(tmpA))
if(tmpA == tmpB):
    print("Yes")
else:
    print("No")