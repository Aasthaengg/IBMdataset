s1, s2, s3 = map(str, input().split())
S1_ord = ord(s1[0])-32
S2_ord = ord(s2[0])-32
S3_ord = ord(s3[0])-32

S1_chr = chr(S1_ord)
S2_chr = chr(S2_ord)
S3_chr = chr(S3_ord)
print(S1_chr + S2_chr + S3_chr)