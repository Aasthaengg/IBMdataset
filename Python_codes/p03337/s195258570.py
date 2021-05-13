A,B = map(int,input().split(" "))
Max = max([A+B, A-B, A*B])
print(Max)