import sys,math
input = sys.stdin.readline

def f(s):
    n = int(s)%2
    return n

N,P = list(map(int,input().split()))
A = list(map(f,input().split()))

c0 = A.count(0)
c1 = A.count(1)
fact = [1]* (c1+1)
for i in range(1,c1+1):
    fact[i]= fact[i-1]*i

cnt = 0
for i in range(P,c1+1,2):
    cnt += fact[c1]//fact[i]//fact[c1-i]

print(cnt*pow(2,c0))
