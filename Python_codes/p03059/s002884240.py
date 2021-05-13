a,b,t = map(int, input().split())
time = 0
i = 0
sum = 0
while True:
    i += 1
    if t + 0.5 < a*i:
        break
    sum += b

print(sum)