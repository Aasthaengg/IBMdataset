N, K = map(int, input().split())
S = input()

rights = []
lefts = []

for i in range(N):
    if i == 0:
        if S[i] == "L":
            now = "L"
            start = i
        else:
            now = "R"
            start = i
    else:
        if S[i] != now:
            end = i
            if now == "R":
                rights.append((start, end))
            else:
                lefts.append((start, end))
            start = i
            now = S[i]
            if i == N-1:
                if now == "R":
                    rights.append((i, i+1))
                else:
                    lefts.append((i, i+1))

n_inner_left = 0
n_inner_right = 0
for left in lefts:
    if (0 not in left) and (N not in left):
        n_inner_left += 1
for right in rights:
    if (0 not in right) and (N not in right):
        n_inner_right += 1
# unhappy
total = 0
if S[0] == "L":
    total += 1
if S[N-1] == "R":
    total += 1
for i in range(N-1):
    if S[i] == "R" and S[i+1] == "L":
        total += 2

rest = K
if n_inner_left > n_inner_right:
    reduce_2 = min(K, n_inner_left)
    total -= 2*reduce_2
    rest -= reduce_2
    if S[0] == "L" and rest > 0:
        total -= 1
elif n_inner_left < n_inner_right:
    reduce_2 = min(K, n_inner_right)
    total -= 2*reduce_2
    rest -= reduce_2
    if S[N-1] == "R" and rest > 0:
        total -= 1
else:
    reduce_2 = min(K, n_inner_left)
    total -= 2*reduce_2
    rest -= reduce_2
    if rest > 0:
        if S[0] == "L" and S[N-1] == "R":
            total -= 1
        if S[0] == "R" and S[N-1] == "L":
            total -= 1


print(N-total)