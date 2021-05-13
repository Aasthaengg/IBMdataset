k, a, b = map(int, input().split())
if a+2>=b:
    print(k+1)
    exit()
k -= a+1
ans = b
ans += (b-a)*(k//2) + k%2
print(ans)