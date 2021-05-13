from collections import Counter

# input
S = list(input())
S = "".join(sorted(S))
T = list(input())
T = "".join(sorted(T))

# check
counter_s = Counter(S).most_common()
counter_t = Counter(T).most_common()

if len(counter_t) != len(counter_s):
    print("No")
elif S == T:
    print("Yes")
else:
    c_match = [True] * len(counter_t)
    for i in range(len(counter_t)):
        co_s = counter_s[i][1]
        co_t = counter_t[i][1]

        if co_s != co_t:
            c_match[i] = False

    if c_match.count(False) == 0:
        print("Yes")
    else:
        print("No")