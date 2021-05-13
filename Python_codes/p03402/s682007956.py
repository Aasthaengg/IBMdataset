A, B = map(int, input().split())
L = []
def AA(A): return [".#" * min(A, 50) + "##" * (50-min(A, 50)), "##" * 50]
def BB(B):  return [".." * 50, "#." * min(B, 50) + ".." * (50-min(B, 50))]
L += AA(max(0, A-1))
A -= 51
while A > 0:
    L += AA(A)
    A -= 50
L += BB(max(0, B-1))
B -= 51
while B > 0:
    L += BB(B)
    B -= 50
print(len(L), 100)
print(*L, sep="\n")