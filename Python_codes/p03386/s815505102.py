# B
a, b, k = map(int, input().split())

ans = []
for i in range(k):  
    ans.append(a+i)
    ans.append(b-i)
    
ans = sorted(set(ans))
for i in ans:
    if a <= i <= b:
        print(i)