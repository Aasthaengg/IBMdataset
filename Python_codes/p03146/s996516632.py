def f(n):
    if n%2==0:
        return n//2
    else:
        return 3*n+1

a = [0]
a.append(int(input()))
for i in range(2,1000001):
    tmp = f(a[i-1])
    if tmp in a:
        break
    a.append(tmp)
#print(a)
print(i)