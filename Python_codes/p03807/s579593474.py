n = int(input())

al = list(map(int,input().split()))

even = 0
odd = 0

for a in al:
    if a % 2 == 0:
        even += 1
    else:
        odd += 1

if even == 0 or odd == 0:
    print("YES")
elif (odd%2) == 0:
    print("YES")
else:
    print("NO")

