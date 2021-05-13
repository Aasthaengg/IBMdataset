def f(x):
    if x%2:
        return 3*x + 1
    else:
        return x/2
s = int(input())
a = [s]
for i in range(1,10**6+2):
    if f(a[i-1]) in a:
        print(i+1)
        break
    a.append(f(a[i-1]))
