from sys import stdout
printn = lambda x: stdout.write(x)
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
DBG = True # and False
BIG = 999999999
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

n,m = inm()
u0 = []
u1 = []
u2 = []
u3 = []
u4 = []
u5 = []
u6 = []
u7 = []
for i in range(n):
    x,y,z = inm()
    u0.append(x+y+z)
    u1.append(x-y+z)
    u2.append(x+y-z)
    u3.append(x-y-z)
    u4.append(-x+y+z)
    u5.append(-x-y+z)
    u6.append(-x+y-z)
    u7.append(-x-y-z)
u0.sort(reverse=True)
u1.sort(reverse=True)
u2.sort(reverse=True)
u3.sort(reverse=True)
u4.sort(reverse=True)
u5.sort(reverse=True)
u6.sort(reverse=True)
u7.sort(reverse=True)
s0 = sum(u0[0:m])
s1 = sum(u1[0:m])
s2 = sum(u2[0:m])
s3 = sum(u3[0:m])
s4 = sum(u4[0:m])
s5 = sum(u5[0:m])
s6 = sum(u6[0:m])
s7 = sum(u7[0:m])
print(max([s0,s1,s2,s3,s4,s5,s6,s7]))
