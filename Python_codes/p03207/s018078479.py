N = int(input())
ls = []
for i in range(N):
    ls.append(int(input()))
ls.sort(reverse=True)
maxa = ls.pop(0)
print(maxa//2+sum(ls))