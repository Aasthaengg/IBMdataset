N = int(input())
A = [int(i) for i in input().split()]

odd_count = 0
for i in A:
    if i % 2 == 1:
        odd_count += 1

if odd_count % 2 == 0:
    print("YES")
else:
    print("NO")