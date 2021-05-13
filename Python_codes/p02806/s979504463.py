n = int(input())
st = [list(input().split()) for i in range(n)]
s = [i[0] for i in st]
t = [int(i[1]) for i in st]
x = input()
SUM = 0
for i in range(s.index(x) + 1, n):
    SUM += t[i]
print(SUM)