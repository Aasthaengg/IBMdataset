k = int(input())
alst = list(map(int, input().split()))[::-1]
l = 2
r = 2

def check(l, r, a):
    if l % a == 0:
        return True
    elif r // a == l // a:
        return False
    else:
        return True

for a in alst:
    if not check(l, r, a):
        print(-1)
        exit()
    l = (l + a - 1) // a * a
    r = r // a * a + (a - 1)
print(l, r)