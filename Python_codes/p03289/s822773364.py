S = input()

def word_check(S):
    for s in S:
        if s.isupper():
            if s not in ["A", "C"]:
                return "WA"
    if S[0] == "A":
        if S[1] not in ["A", "C"] and S[-1] not in ["A", "C"]:
            count_C = 0
            for s in S[2: -1]:
                if s == "C":
                    count_C += 1
            if count_C == 1:
                return "AC"
    return "WA"

print(word_check(S))