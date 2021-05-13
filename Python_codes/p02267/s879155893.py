def linear_search(li, value):
    for x in li:
        if x == value:
            return True
    return False

input() # n
S = [int(x) for x in input().split()] 
input() # q
T = [int(x) for x in input().split()]

ans = 0

for x in T:
    if linear_search(S, x):
        ans += 1

print(ans)