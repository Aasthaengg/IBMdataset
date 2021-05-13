import sys
def S(): return sys.stdin.readline().rstrip()

s1,s2,s3 = map(str,S().split())
print((s1[0]+s2[0]+s3[0]).upper())
