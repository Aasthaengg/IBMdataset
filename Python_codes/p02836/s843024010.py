def resolve():
    S = input()
    s = len(S)
    count = 0
    if s%2 == 0:
        for i in range(s//2):
            if S[i] != S[(i+1)*-1]:
                count += 1
    else:
        for i in range((s-1)//2):
            if S[i] != S[(i+1)*-1]:
                count += 1
    print(count)
resolve()
