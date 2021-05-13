def solve():
    ans = 0
    X = input()
    num = 0
    for x in X:
        if x=='S':
            num += 1
        else:
            if num>0:
                num -= 1
    ans = num*2
    return ans
print(solve())