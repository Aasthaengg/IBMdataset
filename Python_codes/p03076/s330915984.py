import itertools

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

l = [a, b, c, d, e]

min_m = 999 * 5
for abcde in itertools.permutations(l, 5):
    # print(abcde)
    end = 0
    for v in abcde:
        mod = end % 10
        if mod != 0:
            end += 10 - mod
        end += v
        # print(end)
    if end < min_m:
        min_m = end
print(min_m)