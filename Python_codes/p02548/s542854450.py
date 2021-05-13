N=int(input())
x = N
n = 1
s = 0
while x > 0:
    x = (N-1)//n
    s += x
    n+=1
print(s)
