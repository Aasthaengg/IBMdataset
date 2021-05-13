a,b,x = map(int, input().split())

bcnt = b // x
acnt = (a-1) // x
print(bcnt-acnt)
