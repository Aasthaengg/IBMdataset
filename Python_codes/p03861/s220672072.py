a,b,x = map(int, input().split())
work1 = b // x
work2 = (a - 1) // x
print(work1 - work2)