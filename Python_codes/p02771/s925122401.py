a, b, c = map(int, input().split())
res = 'No'
if a == b and a != c: res = 'Yes'
if a == c and a != b: res = 'Yes'
if c == b and a != c: res = 'Yes'
print(res)