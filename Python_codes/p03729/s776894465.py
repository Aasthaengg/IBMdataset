import sys
str_array = list(map(str,input().split()))

for I in str_array:
    if not I.islower():
        sys.exit()
    if len(I) < 0 or len(I) > 10:
        sys.exit()

result = "YES"
last = ""
first = ""
for J in range(len(str_array)-1):
    first = str_array[J+1][0]
    last = str_array[J][-1]
    if not last == first:
        result = "NO"

print(result)