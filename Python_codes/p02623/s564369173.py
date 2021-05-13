from copy import deepcopy as dp
n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_sum = [0]
for i in a:
    if a_sum[-1] + i > 10 ** 9:
        break
    a_sum.append(a_sum[-1] + i)

b_sum = [0]
for i in b:
    if b_sum[-1] + i > 10 ** 9:
        break
    b_sum.append(b_sum[-1] + i)

class binarySearch(object):

    def __init__(self, target):
        self.target = dp(target)
        self.target.append(10**18)

    def set(self, value):
        self.value = value

    def search(self):
        self.lower, self.upper = 0, len(self.target) - 1
        while self.upper != self.lower+1:
            next = (self.upper + self.lower) // 2
            if self.target[next] > self.value:
                self.upper = next
            else:
                self.lower = next
        return self.lower


test = binarySearch(b_sum)

ans = 0
for i, a_time in enumerate(a_sum):
    rest = k - a_time
    if rest >= 0:
        test.set(rest)
        ans = max(i + test.search(), ans)
    else:
        break

print(ans)