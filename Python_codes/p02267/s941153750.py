# ALDS1 : Linear Search

n = input()
S = set(map(int,raw_input().split()))
q = input()
T = set(map(int,raw_input().split()))

print len(S & T)