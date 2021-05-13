N = int(input())
for i in reversed(range(1, 10)):
    if N % i == 0:
        N //= i
        break
if N < 10:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)