S = list(input())
ACGT = ["A", "C", "G", "T"]
count = 0
Max = 0
if len(S) == 1:
    if  S[0] in ACGT:
        print(1)
    else:
        print(0)
else:
    for s in S:
        if s in ACGT:
            count += 1
            if count > Max:
                Max = count
        else:
            if count > Max:
                Max = count
            count = 0
    print(Max)