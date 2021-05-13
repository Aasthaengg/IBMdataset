n = int(input())
l = list(map(int, input().split()))

def check(l):
    return 'Yes' if max(l) < sum(l) - max(l) else 'No'

print(check(l))