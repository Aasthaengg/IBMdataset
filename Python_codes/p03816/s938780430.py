import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり


N = I()
A = LI()

from collections import Counter

c = Counter(A)

a = 0  # 消さねばならない文字数
for i in c.keys():
    a += c[i]-1

print(N-2*((a+1)//2))