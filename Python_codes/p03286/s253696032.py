n = int(input())
if n == 0:
    print(0)
    exit()
ans = []
while abs(n) > 0:
    ans.append(n%2)
    n = (n - (n % 2)) // -2
print(''.join(map(str, ans[::-1])))
