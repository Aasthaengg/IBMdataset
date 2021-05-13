# Sol : (n1 + n2)/2
# Ex : 
# Q : 16 - x = 2 - x
# => 16 + x = 2 + x
# => 16 + 2 = 2x
# => 18/2 = x
# => 9 = x
a = list(map(int, input().split()))
if ((a[0] + a[1]) // 2) * 2 != a[0] + a[1]:
    print("IMPOSSIBLE")
else:
    print(((a[0] + a[1]) // 2))