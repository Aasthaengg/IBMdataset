abc = list(map(int, input().split()))
abc.sort()
ans = abc[2] - abc[1]
abc[0] += ans

if (abc[2]-abc[0]) % 2 == 0:
    ans += (abc[2]-abc[0]) // 2
else:
    ans += (abc[2]-abc[0]) // 2 + 2

print(ans)
