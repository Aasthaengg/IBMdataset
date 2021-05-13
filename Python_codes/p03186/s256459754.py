A,B,C = map(int,input().split())

if (A+B)+1>=C:
    print(B+C)
    exit()
print(B+((A+B)+1))
