S = input()

cand = set()
def make(F, B):
    if len(B) == 0:
        cand.add(F)
        return
    if B[0] == "A":
        make(F, B[1:])
    make(F + B[0], B[1:])

make("", "AKIHABARA")

if S in cand:
    print("YES")
else:
    print("NO")