S = [input() for _ in range(3)]
for i in range(3):
    S[i] = list(S[i])
p = 0 #プレイヤー
while True:
    if not S[0] and p == 0:
        print("A")
        break
    if not S[1] and p == 1:
        print("B")
        break
    if not S[2] and p == 2:
        print("C")
        break
    p_t = S[p].pop(0)
    if p_t == "a":
        p = 0
    elif p_t == "b":
        p = 1
    elif p_t == "c":
        p = 2