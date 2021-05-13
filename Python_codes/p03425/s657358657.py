N = int(input())
march_dict = {
    'M': 0,
    'A': 0,
    'R': 0,
    'C': 0,
    'H': 0
}
for i in range(N):
    S = input()
    s_head = S[0]
    if march_dict.get(s_head) is not None:
        march_dict[s_head] += 1

march_candidate = [key for key, val in march_dict.items() if val != 0]

import itertools

ans = 0
for C in itertools.combinations(march_candidate, 3):
    a = march_dict[C[0]]
    b = march_dict[C[1]]
    c = march_dict[C[2]]
    ans += a * b * c
    #print(ans)
    #print(march_candidate)
print(ans)
