w = [str(input()) for i in range(5)]
num = ['0','9','8','7','6','5','4','3','2','1']
w1 = []
m = 0
t = 0
for h in w:
    for j in num:
        if h[-1] == j:
            w1.append(int(h)+num.index(j))
            if m <= num.index(j):
                m = num.index(j)
                k = w.index(h)
for l in range(5):
    if l != k:
        t += w1[l]
print(t+int(w[k]))