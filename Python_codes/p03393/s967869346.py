from string import ascii_lowercase
def next_permutation(a):
    """Generate the lexicographically next permutation inplace.

    https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
    Return false if there is no next permutation.
    """
    # Find the largest index i such that a[i] < a[i + 1]. If no such
    # index exists, the permutation is the last permutation
    for i in reversed(range(len(a) - 1)):
        if a[i] < a[i + 1]:
            break  # found
    else:  # no break: not found
        return -1  # no next permutation

    # Find the largest index j greater than i such that a[i] < a[j]
    j = next(j for j in reversed(range(i + 1, len(a))) if a[i] < a[j])
    
    return a[:i] + a[j]

s = input()
lower = set(ascii_lowercase)
for c in s:
    if c in lower:
        lower.remove(c)
    else:
        print(-1)
        exit()
if len(lower) > 0:
    lower = sorted(lower)
    print(s+lower[0])

else:
    print(next_permutation(s))