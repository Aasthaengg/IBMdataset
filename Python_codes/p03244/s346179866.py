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
    
    odds_modes= Counter(odds).most_common(2)
    evens_modes = Counter(evens).most_common(2)

    if odds_modes[0][0] != evens_modes[0][0]:
        print(len(odds)- odds_modes[0][1] + len(evens) - evens_modes[0][1])
    else:
        odds_modes.append((-1,0))
        evens_modes.append((-1,0))

        print(
            min(
                len(odds)-odds_modes[0][1] + len(evens) - evens_modes[1][1],
                len(odds)-odds_modes[1][1] + len(evens) - evens_modes[0][1],
            )
        )
            

main()