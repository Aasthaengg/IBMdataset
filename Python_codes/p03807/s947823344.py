N = int(input())
A = list(map(int, input().split()))

odd_count = 0
even_count = 0

for i in A:
    if i%2==1:
        odd_count += 1
    else:
        even_count += 1

if odd_count%2==1:
    print("NO")
else:
    print("YES")