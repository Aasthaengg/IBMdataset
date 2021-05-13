n, y = map(int,input().split())
y = y//1000
for i in range(n+1):
    for j in range (n+1-i):
        k = n - i - j
        if 10*i + 5* j + 1 * k == y:
            print(str(i) +' '+str(j)+' '+str(k))
            exit()
print('-1 -1 -1')