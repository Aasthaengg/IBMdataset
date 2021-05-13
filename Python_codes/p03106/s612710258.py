A,B,K = map(int,input().split())
li = [x for x in range(1,A+1) if A%x == 0 and B%x == 0]
print(li[-K])
