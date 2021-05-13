# 085 B
N = int(input())
dd=[list(map(int,list(input()))) for i in range(N)]
d = sorted(dd)
c = 1
for i in range(N-1):
    if d[i] != d[i+1]:
        c += 1
print(c)