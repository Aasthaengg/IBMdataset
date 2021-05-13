n = int(input())
s = list(map(int,input().split()))

odd = []
even = []
for i in range(n):
    if i%2 == 0:
        odd.append(s[i])
    else:
        even.append(s[i])
    
if n%2 == 1:
    ans = odd[::-1] + even
else:
    ans = even[::-1] + odd
    
ans_str=[str(a) for a in ans]
print(" ".join(ans_str))

