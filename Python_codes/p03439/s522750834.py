# インタラクティブ
n = int(input())

top    = n
bottom = 0
print(0)
s = input()
sex = [-1]*(n+1)
if s == 'Vacant':
    exit(0)
elif s == 'Male':
    sex[0] = sex[n] = 0
else:
    sex[0] = sex[n] = 1

while top - bottom > 1:
    mid = (top+bottom)//2
    print(mid)
    s = input()
    if s  == 'Vacant':
        exit(0)
    elif s == 'Male':
        sex[mid] = 0
    else:
        sex[mid] = 1
    if (sex[top]^sex[mid]) ^ ((top - mid)%2):
        bottom = mid
    else:
        top = mid

print(bottom)
s = input()
if s != 'Vacant':
    print(top%n)
    s = input()
