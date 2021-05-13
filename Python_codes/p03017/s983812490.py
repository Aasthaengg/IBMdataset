N, A, B, C, D = map(int, input().split())
S = list(input())
A -= 1
B -= 1
C -= 1
D -= 1

def check_one_people_can(start, end):
    s = S[start+1: end]
    before_sharp = False
    for x in s:
        if x == "#":
            if before_sharp:
                return False
            before_sharp = True
        else:
            before_sharp = False
    return True

def check_triple_dots(start, end):
    s = S[start-1: end+2]
    continuous_dots = 0
    for x in s:
        if x == ".":
            continuous_dots += 1
            if continuous_dots == 3:
                return True
        else:
            continuous_dots = 0
    return False

if D > C:
    if check_one_people_can(A, C) and check_one_people_can(C, D):
        print("Yes")
    else:
        print("No")
else:
    if check_triple_dots(B, D) and check_one_people_can(A, C):
        print("Yes")
    else:
        print("No")
