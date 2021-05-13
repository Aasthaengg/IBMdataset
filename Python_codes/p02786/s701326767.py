h = int(input())

def hp(n):
    if n == 1:
        ans = 1
    else:
        ans = 2*hp(n//2) + 1
    return ans
print(hp(h))