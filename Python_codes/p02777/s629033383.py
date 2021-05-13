x = dict()
s,t = input().split()
n,m = map(int, input().split())
x[s] = n
x[t] = m
p = input()
x[p] -= 1
print(x[s], x[t])