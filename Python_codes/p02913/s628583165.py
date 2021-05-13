n = int(input())
s = input()
def output():
    left, right = 0, n//2+1
    while left < right-1:
        mid = (left+right)//2
        if check(mid):
            left = mid
        else:
            right = mid
    return left
def check(x):
    hashes = set()
    for i in range(n - 2*x + 1):
        hashes.add(s[i: i+x])
        if s[i+x: i+2*x] in hashes:
            return True
    return False
print(output())