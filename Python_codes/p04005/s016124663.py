A,B,C = map(int, input().split())

if A*B*C%2==0:
    print(0)
    exit()

mylist=[A*B,B*C,A*C]
print(min(mylist))