a, b ,t = map(int, input().split())
c = a
t += 0.5
sum_ans = 0
count = 1
while True:
    if a <=  t:
        sum_ans += b
    else:
        break
    count += 1
    a = c*count
print(sum_ans)