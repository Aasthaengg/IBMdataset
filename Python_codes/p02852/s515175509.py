# input
n , m = map(int, list(input().split()))
s = list(map(int, list(input())))[::-1]

# process
ans = [0]

p = 0
i = -1
while p < n:
    j = m
    while True:
        if p+j < n+1 and s[p+j] == 0:
            ans.append(j)
            p += j
            i += 1
            break
        
        j -= 1        
        if j == 0:
            if ans[i] > 1:
                ans[i] -=1
                p -= 1
            else:
                ans = [-1]
                break

    if ans[0] == -1:
        break

# output
if ans[0] == -1:
    print("-1")
else:
    ans.pop(0)
    print(" ".join(map(str, (ans[::-1]))))

