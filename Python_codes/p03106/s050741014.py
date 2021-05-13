a,b,k = map(int, input().split())

output = []
mins = min(a,b)
for divisor in range(1, mins+1):
    if a % divisor == 0 and b % divisor == 0:
        output.append(divisor)
print(output[-k])