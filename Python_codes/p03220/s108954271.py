n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))

def htemp(h):
    return abs(a - ((t * 1000) - (h * 6)) / 1000)

ans = list(map(htemp, h))
ans1 = ans.index(min(ans)) + 1

print(ans1)
