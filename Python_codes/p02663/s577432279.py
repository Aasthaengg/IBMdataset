import sys
input=sys.stdin.readline
h1,m1,h2,m2,k=map(int,input().split())
h1=h1*60
h2=h2*60
m1+=h1
m2+=h2
print(m2-m1-k)