N = int(input())

As = list(map(int,input().split()))
sorted_As = sorted(As,reverse = True)

sum = 0
for i in range(N-1):
    if i == 0:
        sum += sorted_As[0]
    elif i % 2 == 1:
        sum += sorted_As[(i+1)//2]
    else:
        sum += sorted_As[i//2]

print(sum)
