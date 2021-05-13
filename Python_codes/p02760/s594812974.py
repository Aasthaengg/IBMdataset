#k = int(input())
#s = input()
#a, b = map(int, input().split())
#l = list(map(int, input().split()))
def bingo(a, b, c):
    if a[0] == b[0] == c[0]:
        return True
    if a[1] == b[1] == c[1]:
        return True
    if a[2] == b[2] == c[2]:
        return True
    if a[0] == a[1] == a[2]:
        return True
    if b[0] == b[1] == b[2]:
        return True
    if c[0] == c[1] == c[2]:
        return True
    if a[0] == b[1] == c[2]:
        return True
    if a[2] == b[1] == c[0]:
        return True
    return False

l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
l3 = list(map(int, input().split()))
n = int(input())
ans = "No"
for i in range(n):
    b = int(input())
    for j in range(3):
        if l1[j] == b:
            l1[j] = 0
        if l2[j] == b:
            l2[j] = 0
        if l3[j] == b:
            l3[j] = 0
    if (bingo(l1,l2,l3)):
         ans = "Yes"

print(ans)


