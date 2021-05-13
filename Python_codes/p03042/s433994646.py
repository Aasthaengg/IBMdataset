S = input()
f = int(S[0]+S[1])
b = int(S[2]+S[3])

def judge(int):
    if 1 <= int <= 12:
        return 0
    else:
        return 1
ref = [judge(f), judge(b)]

if ref == [1, 1]:
    print("NA")
elif ref == [0, 1]:
    print("MMYY")
elif ref == [1, 0]:
    print("YYMM")
else:
    print("AMBIGUOUS")
