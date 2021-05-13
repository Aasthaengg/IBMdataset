def triple_dots():
    K = int(input())
    S = input()
    if K >= len(S):
        print(S)
    else:
        s = S[:K]
        s = s + "..."
        print(s)
        
triple_dots()