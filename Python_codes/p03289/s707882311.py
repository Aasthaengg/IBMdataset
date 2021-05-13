from collections import Counter

S = input()

def judge(S):
    if S[0] != 'A':
        return False
    elif Counter(S[2:-1])['C'] != 1:
        return False
    elif any(v != 'C' and not v.islower() for v in S[1:]) or not S[1].islower() or not S[-1].islower():
        return False
    return True

print('AC' if judge(S) else 'WA')