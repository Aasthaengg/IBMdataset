def main():
    from collections import Counter
    n = int(input())
    V = map(int,input().split())
    odds = []
    evens = []
    for i,v in enumerate(V):
        if i & 1:
            evens.append(v)
        else:
            odds.append(v)
    
    odds_counter = list(Counter(odds).items())
    eves_counter = list(Counter(evens).items())
    
    odds_counter.sort(reverse=True, key= lambda x: x[1])
    eves_counter.sort(reverse=True, key= lambda x: x[1])

    if odds_counter[0][0] != eves_counter[0][0]:
        print(len(odds)- odds_counter[0][1] + len(evens) - eves_counter[0][1])
    else:
        odds_counter.append((-1,0))
        eves_counter.append((-1,0))

        print(
            min(
                len(odds)-odds_counter[0][1] + len(evens) - eves_counter[1][1],
                len(odds)-odds_counter[1][1] + len(evens) - eves_counter[0][1],
            )
        )
            
        

    

    
    
    


main()