import copy
n = int(input())
t = list(map(int,input().split()))
m = int(input())
for i in range(m):
    c_t = copy.deepcopy(t)
    p,x = list(map(int,input().split()))
    c_t[p-1]=x
    print(sum(c_t))