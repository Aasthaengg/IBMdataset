n = int(input())
s = input()
s2 = s[:n//2]
s3 = s[n//2:]
print("Yes") if s2 == s3 else print("No")