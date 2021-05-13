n = int(input())
s1 = input()
s2 = input()
s3 = input()
ans = 0
for i in range(n):
    if s1[i] == s2[i] and s2[i] == s3[i] and s3[i] == s1[i]:
        True
    elif s1[i] != s2[i] and s2[i] != s3[i] and s3[i] != s1[i]:
        ans += 2
    else:
        ans += 1
print(ans)