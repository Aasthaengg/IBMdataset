X = int(input())

ans = 8
rate = 600
while X >= rate:
    ans -= 1
    rate += 200
print(ans)
