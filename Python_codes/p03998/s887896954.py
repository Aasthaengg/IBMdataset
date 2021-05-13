S = {c: list(input()) for c in 'abc'}
s = "a"
while(S[s]):
    s = S[s].pop(0)
    if(S[s] == []):
        print(s.upper())
        break
