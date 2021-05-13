n = int(input())

ans = []
for i in range(1,10**6+1):
    if n % i == 0:
        ans.append(i+(n//i)-2)

print(min(ans))
