from collections import Counter

n = int(input())

a = Counter(map(int, input().split()))

def thankyou():
    for k, v in a.items():
        if k > v:
            yield v
        else:
            yield v - k

print(sum(thankyou()))