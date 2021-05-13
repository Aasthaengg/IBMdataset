def next_permutation(case):
    for index in range(1, len(case)):
        Px_index = len(case) - 1 - index
        # Start travelling from the end of the Data Structure
        Px = case[-index - 1]
        Px_1 = case[-index]

        # Search for a pair where latter the is greater than prior
        if Px < Px_1:
            suffix = case[-index:]
            pivot = Px
            minimum_greater_than_pivot_suffix_index = -1
            suffix_index = 0

            # Find the index inside the suffix where ::: [minimum value is greater than the pivot]
            for Py in suffix:
                if pivot < Py:
                    if minimum_greater_than_pivot_suffix_index == -1 or \
                            suffix[minimum_greater_than_pivot_suffix_index] >= Py:
                        minimum_greater_than_pivot_suffix_index = suffix_index
                suffix_index += 1
            # index in the main array
            minimum_greater_than_pivot_index = minimum_greater_than_pivot_suffix_index + Px_index + 1

            # SWAP
            temp = case[minimum_greater_than_pivot_index]
            case[minimum_greater_than_pivot_index] = case[Px_index]
            case[Px_index] = temp

            # Sort suffix
            new_suffix = case[Px_index + 1:]
            new_suffix.sort()

            # Build final Version
            new_prefix = case[:Px_index + 1]
            next_permutation = new_prefix + new_suffix
            return next_permutation
        elif index == (len(case) - 1):
            # This means that this is at the highest possible lexicographic order
            return False


s = input()
if s == "zyxwvutsrqponmlkjihgfedcba":
    print(-1)
elif len(s) != 26:
    used = [False] * 26
    for i in range(len(s)):
        used[ord(s[i]) - ord("a")] = True
    for i in range(26):
        if used[i] is False:
            s += chr(ord("a") + i)
            print(s)
            break
else:
    dat = []
    for i in range(len(s)):
        dat.append(ord(s[i]) - ord("a"))
    #print(dat)
    #print(next_permutation(dat))
    dat = next_permutation(dat)
    res = ""
    t = "".join(list(map(lambda x: chr(ord("a") + x), dat)))
    for i in range(26):
        print(t[i], end="")
        if s[i] != t[i]:
            break
    print("")

