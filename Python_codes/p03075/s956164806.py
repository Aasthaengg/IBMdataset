import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = int(input())

li = [a,b,c,d,e]

ans = False
for i in range(5):
    for j in range(i + 1, 5):
        if li[j] - li[i] > k:
            ans = True
            break


if ans:
    print(":(")
else:
    print("Yay!")
