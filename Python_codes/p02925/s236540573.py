def main():
    from sys import setrecursionlimit, stdin, stderr
    from os import environ
    from collections import defaultdict, deque, Counter
    from math import ceil, floor
    from itertools import accumulate, combinations, combinations_with_replacement
    setrecursionlimit(10**6)
    dbg = (lambda *something: stderr.write("\033[92m{}\033[0m".format(str(something)+'\n'))) if 'TERM_PROGRAM' in environ else lambda *x: 0
    input = lambda: stdin.readline().rstrip()
    LMIIS = lambda: list(map(int,input().split()))
    II = lambda: int(input())
    P = 10**9+7
    INF = 10**18+10

    N = II()
    A = []
    match = defaultdict(lambda : -1)
    for i in range(N):
        a = deque(map(lambda x: int(x)-1, input().split()))
        match[i] = a[0]
        A.append(a)
    

    ans = 0
    players = deque(range(N))

    matched = True
    while matched and len(players) > 0:
        matched = False
        next_players = deque()
        next_match = defaultdict(lambda : -1)

        for i in players:
            if match[i] == -1:
                continue
            a = A[i]
            j = a[0]
            b = A[j]

            if match[j] == i:
                a.popleft()
                b.popleft()
                matched = True
                match[i] = -1
                match[j] = -1
                if len(a) > 0:
                    next_match[i] = a[0]
                    next_players.append(i)

                if len(b) > 0:
                    next_match[j] = b[0]
                    next_players.append(j)

        players = next_players
        match.update(next_match)
        ans += 1


        
    print(ans if matched and len(next_players)==0 else -1)








    

    ans = 0

    

    
   
main()