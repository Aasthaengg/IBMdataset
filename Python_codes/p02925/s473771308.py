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
    for i in range(N):
        A.append(deque(map(lambda x: int(x)-1, input().split())))
    
    dbg('hoge')
    ans = 0
    players = deque(range(N))
    calc = 0
    
    match = defaultdict(lambda : -1)
    first = True
    while True:
        mathced = False
        next_players = deque()
        next_match = defaultdict(lambda : -1)
        # dbg('day',ans)
        for i in players:
            # dbg(i,ans,players,A,match)
            calc += 1
            a = A[i]
            if len(a) == 0:
                continue
            j = a[0]
            b = A[j]

            
            
            if match[j] == i and match[i] == j:
                # dbg(i,j)
                b.popleft()
                # if b[0] != i:
                #     dbg('fuga')
                a.popleft()
                mathced = True
                match[i] = -1
                match[j] = -1
                if len(a) > 0:
                    next_match[i] = a[0]
                    next_players.append(i)

                if len(b) > 0:
                    next_match[j] = b[0]
                    next_players.append(j)


            else:
                next_match[i] = a[0]

        players = next_players
        match.update(next_match)
        if first:
            dbg('hogehoge')
            first = False
            players = range(N)
            continue
        ans += 1
        if not mathced or len(players) == 0:
            break

        
    print(ans if mathced and len(next_players)==0 else -1)
    dbg(calc,mathced,len(next_players),len(a),len(b))







    

    ans = 0

    

    
   
main()