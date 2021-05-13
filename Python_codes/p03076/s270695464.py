ans = 0
x = []
y = []
for i in range(5):
    x.append(int(input()))
    y.append(x[i]%10)

for i in range(5):
    if y[i] == 0:
        ans += x[i]
    else:
        ans += x[i]-y[i]+10
m = 10
for i in y:
    if i == 0:
        continue
    else:
        m = min(m,i)
if m == 10:
    print(ans)
else:
    print(ans+m-10)