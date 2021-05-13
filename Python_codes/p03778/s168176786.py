s = input().split()

w = int(s[0])
a = int(s[1])
b = int(s[2])

answer = 0

if a + w < b:
    answer = b - (a + w)
else:
    answer = a - (b + w)

if (a <= b and b <= a + w) or (a <= b + w and b + w <= a + w):
    answer = 0
    
print(answer)
