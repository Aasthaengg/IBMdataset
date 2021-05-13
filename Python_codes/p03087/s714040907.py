n,q = map(int,input().split())
s = input()
lr = [list(map(int,input().split())) for _ in range(q)]

acli = [0]*n
for i in range(1,n):
    if s[i] == "C" and s[i-1] == "A":
        acli[i] = acli[i-1] + 1
    else:
        acli[i] = acli[i-1]

for x in lr:
    print(acli[x[1]-1]-acli[x[0]-1])