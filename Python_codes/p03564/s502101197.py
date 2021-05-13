n = int(input())
k = int(input())
ans = 1
for i in range(n):
    num1 = ans*2
    num2 = ans+k
    ans = min(num1,num2)
print(ans)