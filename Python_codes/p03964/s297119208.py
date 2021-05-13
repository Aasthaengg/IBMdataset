import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N = I()
x,y = LI()  # 高橋君、青木君の得票数
for i in range(1,N):
    T,A = LI()
    a = max((x+T-1)//T,(y+A-1)//A)
    x,y = T*a,A*a

print(x+y)