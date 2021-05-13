s1 = input()
s1r = s1[::-1]
n1 = len(s1)
s2 = s1[:(n1-1)//2]
s2r = s2[::-1]
s3 = s1[-(n1-1)//2:]
s3r = s3[::-1]
if s1 == s1r and s2 == s2r and s3 == s3r:
    print('Yes')
else:
    print('No')