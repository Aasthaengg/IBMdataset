s1, s2, s3 = input().split()

S1 = []
for _ in s1:
  S1.append(_)
S2 = []
for _ in s2:
  S2.append(_)
S3 = []
for _ in s3:
  S3.append(_)
  
ans = S1[0]+S2[0]+S3[0]
print(str.upper(ans))