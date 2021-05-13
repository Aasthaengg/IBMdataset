s = input()
a = [int(c) for c in s]
mark = ['+', '-']
sum = 0
ans = 0
for i in range(2**3):
    sum = int(a[0])
    for j in range(3):
        k = (i >> j)
        sum += int(a[j+1])*(-1)**k
    if sum == 7:
        ans = i
        break
# print(i)
# 下からn桁目のビットが1:-
# 下からn桁目のビットが0:+
b = []
m = []
formula = ''
for l in range(3):
    b.append(str(a[l+1]))
    c = (ans >> l & 1)
    m.append(mark[c])
    formula += (m[l] + b[l])
print(str(a[0]) + formula + '=7')