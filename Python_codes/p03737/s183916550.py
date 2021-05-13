import sys
S = list(map(str,input().split()))

for I in S:
    if not I.islower():
        sys.exit()
    if len(I) < 0 or len(I) > 10:
        sys.exit()

result = ""
for J in S:
    result = result + J[0:1]
print(result.upper())