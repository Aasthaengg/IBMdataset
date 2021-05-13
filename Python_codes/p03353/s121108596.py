S = input()
K = int(input())

lS = len(S)
asc = 97
while True:
    st = set()
    for i in range(lS):
        if S[i] == chr(asc):
            j = i + 1
            while j - i <= 5 and j <= lS:
                st.add(S[i:j])
                j += 1
    if len(st) >= K:
        print(sorted(list(st))[K - 1])
        break
    else:
        K -= len(st)
        asc += 1
