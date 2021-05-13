r, g, b = [int(x) for x in input().split()]
times = int(input())

def check(r, g, b, times):
    while True:
        if b > g > r:
            return 'Yes'
        elif b <= g:
            times -= 1
            b *= 2
        elif g <= r:
            times -= 1
            g *= 2
        if times < 0:
            return 'No'

print(check(r, g, b, times))