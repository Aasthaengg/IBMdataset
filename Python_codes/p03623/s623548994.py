x,a,b = map(int,input().split())
DisA = abs(x-a)
DisB = abs(x-b)
print("A" if DisA < DisB else "B")