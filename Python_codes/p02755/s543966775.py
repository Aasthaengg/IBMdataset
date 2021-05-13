from math import floor
A_tax, B_tax = map(int,input().split())

for i in range(1,1001):
    if floor(i*0.08) == A_tax and floor(i*0.1) == B_tax:
        print(i)
        exit()

print(-1)