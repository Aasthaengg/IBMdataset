N,x = map(int, input().split())
li = list(map(int, input().split()))
li.sort()
a = 0
an = 0
while a < N:
    x -= li[a]
    if x < 0:
        break
    an += 1
    a += 1
if x > 0:
    an -= 1
print(an)