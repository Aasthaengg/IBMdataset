x = int(input())
cnt = 0

a = int(x/11)
cnt = a*2
x -= 11*a
if x == 0:
    cnt += 0
elif x < 7:
    cnt += 1
else:
    cnt += 2
print(cnt)
