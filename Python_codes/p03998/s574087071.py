S = {"a": input(), "b": input(), "c": input()}

t = "a"
while S[t]:
    nt = S[t][0]
    S[t] = S[t][1:]
    t = nt

else:
    print(t.upper())