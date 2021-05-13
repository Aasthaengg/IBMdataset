# solution
import io
nim, mike, kite = map(int, input().split())
array = list(map(int, input().split()))
    
ans = 0
for i in range(1, nim):
    ans += min((array[i] - array[i - 1]) * mike, kite)
print(ans)