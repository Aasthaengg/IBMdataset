n = int(input())
if n == 0:
    print(0)
    exit()
i = 0
#for i in range(10):
ans = []
while abs(n) > 0:
    #print(n, n // (2 * (-1)**i), n % (2 * (-1)**i))
    #print(n, n % (2 * (-1)**i), n % 2)
    ans.append(n%2)
    #n = n // (2 * (-1)**i)
    n = (n - n % (2 * (-1)**i)) // 2
    i += 1
#print(n, n % (2 * (-1)**i))
#print(ans[::-1])
print(''.join(map(str, ans[::-1])))
