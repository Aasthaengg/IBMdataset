s = list(map(int, input().split()))
s1 = s[0]*s[2]
s2 = s[0]*s[3]
s3 = s[1]*s[2]
s4 = s[1]*s[3]
print(max(s1,s2,s3,s4))