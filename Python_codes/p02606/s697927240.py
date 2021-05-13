import sys

def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

L,R,d = LI()
print(R//d-(L-1)//d)