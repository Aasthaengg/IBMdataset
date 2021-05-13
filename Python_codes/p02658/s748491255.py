N = int(input())
l = list(map(int, input().split()))
if 0 in l:
    print(0)
    exit() 

result = 1

for i in l:
    result *= i
    if result > 10**18:
        print(-1)
        exit() 

print(result)