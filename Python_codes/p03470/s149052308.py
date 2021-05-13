N = int(input())
ls = []
for i in range(N):
    d_i = int(input())
    if d_i not in ls:
        ls.append(d_i)
print(len(ls))