k = int(input())
a = list(map(int, input().split()))

def solve(num, checker):
    return checker*(num//checker)

max_A = max(a)

left, right = 0, k*max_A + 1
while left < right:
    middle = (left+right)//2
    num = middle
    for i in a:
        num = solve(num, i)
    if num >= 2:
        right = middle
    else:
        left = middle + 1
x = right

left, right = 0, k*max_A + 1
while left < right:
    middle = -((-left-right)//2)
    num = middle
    
    for i in a:
        num = solve(num, i)
    if num <= 2:
        left = middle
    else:
        right = middle - 1
        
y = right

if y < x:
    print(-1)
else:
    print(x, y)