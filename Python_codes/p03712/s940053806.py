def invr():
    return(map(int, input().split()))


def insr():
    s = input()
    return(list(s[:len(s)]))


strs = []
a, b = invr()

for i in range(a):
    s = input()
    strs.append(s)
print("#"*(b+2))
for s in strs:
    print("#"+s+"#")
print("#"*(b+2))
