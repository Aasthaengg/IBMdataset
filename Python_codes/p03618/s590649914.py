import collections
def solve(A):
    counter = collections.Counter()
    ans = 1
    for i, a in enumerate(A):
        c = counter[a] if a in counter else 0
        ans += i - c
        counter.update([a])
    return ans
#
# assert(solve("a") == 1)
# assert(solve("aa") == 1)
# assert(solve("ab") == 2)
# print(solve("aatt"))

if __name__ == "__main__":
    A = input()
    print(solve(A))
