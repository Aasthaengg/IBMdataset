import sys
n=int(sys.stdin.readline())
money=100000
for i in range(n):
    money*=1.05
    money=int(money)
    mod = money%1000
    money=money//1000
    if mod>0:
        money+=1
    money=money*1000
print (money)