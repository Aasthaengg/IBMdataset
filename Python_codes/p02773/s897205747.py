N=int(input())
votes = dict()
for _ in range(N):
    S = input()
    if votes.get(S):
        votes[S] += 1
    else:
        votes[S] = 1
max = 0
for k in votes:
    if votes[k] > max:
        max = votes[k]
keys = []
for k in votes:
    if votes[k] == max:
        keys.append(k)
keys.sort()
for k in keys:
    print(k)
