N = int(input())
A = list(map(int, input().split()))

even = 0
odd = 0
for a in A:
    if a % 2 == 0:
        even += 1
    else:
        odd += 1

odd_rest = odd % 2
even += odd // 2
even_rest = even % 2

if (odd_rest + even_rest) == 2:
    print("NO")
else:
    print("YES")
