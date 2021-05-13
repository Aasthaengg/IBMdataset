N = int(input())
A = list(map(int, input().split()))

pre = 0
answer = 0
for a in A:
    if pre == a:
        answer += 1
        pre = 101
    else:
        pre = a
    
print(answer)