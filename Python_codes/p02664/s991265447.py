def resolve():
    S = input()
    s = [ "P" if i =="P" else "D"   for i in S]
    print("".join(s))
resolve()
