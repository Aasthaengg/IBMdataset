N,M = map(int, input().split())
vote_list = [int(i) for i in input().split()]
vote_list.sort(reverse=True)

Mth_got_vote = vote_list[M - 1]

if Mth_got_vote < sum(vote_list) / (4 * M):
    print("No")
else:
    print("Yes")