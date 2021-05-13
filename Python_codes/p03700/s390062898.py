N, A, B = map(int, input().split())
h = []
for i in range(N):
    h.append(int(input()))
    
left = 0
right = max(h)

def can_kill(count):
    ness = 0
    for hp in h:
        ness += max(-(-(hp - B * count) // (A - B)), 0)
    if ness <= count:
        return True
    return False
    
while right - left > 1:
    middle = left + (right - left) // 2
    if can_kill(middle):
        right = middle
    else:
        left = middle

print(right)