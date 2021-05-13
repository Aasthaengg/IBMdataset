n,k = map(int,input().split())
if n / 2 + 1 > k and not (n == 2 and k == 2):
    print("YES")
elif n == 2 and k == 2:
    print("NO")
else:
    print("NO")