n, a, b = list(map(int, input().split()))
sum = 0

for i in range(n+1):
    s_sum = 0
    c = i
    while c>0:
        s_sum += c%10
        c = c//10
    if a <= s_sum <= b:
        sum += i
print(sum)
