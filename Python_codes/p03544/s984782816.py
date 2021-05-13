n = int(input())

if n == 0:
    print('2')
elif n == 1:
    print('1')
else:
    L = [2,1]
    for i in range(n-1):
        tmp = L[i] + L[i+1]
        L.append(tmp)
    print(max(L))