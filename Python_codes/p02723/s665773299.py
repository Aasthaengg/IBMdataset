S =input().strip()

def check(i, j):
    if S[i] == S[j]:
        return True
    return False

if check(2,3) and check(4,5):
    print("Yes")
else:
    print("No")
