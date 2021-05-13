s1 = str(input())
s2 = list(reversed(input()))
s3 = "".join(s2)
if s1 == s3:
    print("YES")
else:
    print("NO")