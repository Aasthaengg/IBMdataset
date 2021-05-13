N,M = map(int,input().split())
A_lis = map(int,input().split())

can_play = N - sum(A_lis)
print(can_play if can_play >= 0 else -1)