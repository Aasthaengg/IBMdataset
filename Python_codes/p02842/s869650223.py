N = int(input())

a = int(N/1.08)

for i in range(a-1, a+2):
    if int(i*1.08) == N:
        result = i
        break
else:
    result = ":("

print(result)
