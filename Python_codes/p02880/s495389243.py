N = int(input())

ans = 'No'
for i in range(1, 9+1):
    if N % i == 0 and N // i < 10:
        ans = 'Yes'
        break

print(ans)
