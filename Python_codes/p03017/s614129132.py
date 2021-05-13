N, A, B, C, D = map(int, input().split())

S = '.' + input() + '#'

# S[A,C],S[B,D]には'##'が存在してはいけない
if '##' in S[A: C + 1] or '##' in S[B: D + 1]:
    print('No')
    exit()

# 追い越さなければいけないとき
# S[B,D]に'...'が存在する必要がある
if D < C:
    if not '...' in S[B - 1 : D + 2]:

        print('No')
        exit()

print('Yes')
