S = input()
ans = [0]*len(S)

even = 0
odd = 0
for i, s in enumerate(S):
    if s == 'R':
        if i%2==0:
            even += 1
        else:
            odd += 1
    else:
        if i%2==0:
            ans[i] += even
            ans[i-1] += odd
        else:
            ans[i] += odd
            ans[i-1] += even
        even = 0
        odd = 0

ans = ans[::-1]
for i, s in enumerate(S[::-1]):
    if s == 'L':
        if i%2==0:
            even += 1
        else:
            odd += 1
    else:
        if i%2==0:
            ans[i] += even
            ans[i-1] += odd
        else:
            
            ans[i] += odd
            ans[i-1] += even
        even = 0
        odd = 0

print(*ans[::-1])